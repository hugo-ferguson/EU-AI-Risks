"""
Break the EU AI Act PDF into segments (chapters, sections, articles,
paragraphs, annexes).
"""

import re
from pathlib import Path

import pdfplumber

from eu_ai_risks.legislation.eu_ai_act.models import Segment

RE_CHAPTER = re.compile(r'^CHAPTER ([IVX]+)$')
RE_SECTION = re.compile(r'^SECTION (\d+)$')
RE_ARTICLE = re.compile(r'^Article (\d+)$')
RE_ANNEX = re.compile(r'^ANNEX ([IVX]+)$')
# Two numbering styles: 'N.' is standard, '(N)' appears in definition articles
RE_PARAGRAPH_DOT = re.compile(r'^(\d+)\.\s')
RE_PARAGRAPH_PAREN = re.compile(r'^\((\d+)\)\s')
RE_POINT = re.compile(r'^\(([a-z])\)\s')
RE_ANNEX_POINT = re.compile(r'^(\d+)\.\s')
# Letters that are also roman numerals, and the numeral that follows each
ROMAN_LETTER_SUCCESSORS = {"i": "ii", "v": "vi", "x": "xi"}
RE_FOOTER = re.compile(r'^(EN\s*$|OJ L,|ELI:|/144)')

ROMAN_TO_INT = {
    "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5,
    "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10,
    "XI": 11, "XII": 12, "XIII": 13,
}


def read_pdf_lines(pdf_path: Path) -> list[str | None]:
    """
    Read all the lines of the .PDF file into a list of line strings.

    :param pdf_path: path to the source .PDF file.
    :return: the list of line strings.
    """

    all_lines = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            for line in (page.extract_text() or "").split("\n"):
                all_lines.append(line.rstrip())
            all_lines.append(None)

    return all_lines


def is_footer(line: str) -> bool:
    """
    Check whether a line is a page footer.

    :param line: the line of text to check.
    :return: whether the line is a footer (these can usually be ignored).
    """
    return bool(RE_FOOTER.search(line))


def find_title_after_heading(
    all_lines: list[str | None], heading_index: int
) -> tuple[int, str]:
    """
    Get the title and its line index that occurs after a heading.
            This will be the chapter or article title.

    :param all_lines: the lines in the .PDF file.
    :param heading_index: the line index of the heading.
    :return: the line index of the title string and its text.
    """

    for i in range(heading_index, len(all_lines)):
        line = all_lines[i]

        # None lines are page breaks; footers never contain titles
        if line is not None and line.strip() and not is_footer(line):
            return i, line.strip()

    return heading_index, ""


def extract_paragraphs(article_segment: Segment) -> list[Segment]:
    """
    Get the numbered paragraphs from an article segment.
    These will be lines inside the body of the article to be trimmed made into
            segments of their own.
    It finds the first numbered paragraph using the regex match, and then
            joins subsequent lines into its paragraph segment.
    Subsequent numbered paragraphs are made into their own segments.

    :param article_segment: the article segment.
    :return: a list of paragraph segments (these do not have titles).
    """

    # Prefer 'N.' style; '(N)' is a fallback for definition articles
    pattern = (
        RE_PARAGRAPH_DOT
        if any(RE_PARAGRAPH_DOT.match(line) for line in article_segment.body)
        else RE_PARAGRAPH_PAREN
    )

    paragraphs = []

    for i, line in enumerate(article_segment.body):
        paragraph_match = pattern.match(line)

        if not paragraph_match:
            continue

        paragraph_num = int(paragraph_match.group(1))
        paragraph_lines = [line]

        for following_line in article_segment.body[i + 1:]:
            if pattern.match(following_line):
                break
            paragraph_lines.append(following_line)

        paragraphs.append(Segment(
            type="paragraph",
            id=f"{article_segment.id}:p{paragraph_num}",
            num=paragraph_num,
            parent_id=article_segment.id,
            body=paragraph_lines,
        ))

    return paragraphs


def _is_roman_sub_point(lines: list[str], index: int, letter: str) -> bool:
    """
    Check whether '(i)', '(v)' or '(x)' starts a roman sub-point, not a letter.

    After point (h) the next letter is (i), but '(i)' there is often the first
    roman sub-point of (h). It is roman when its roman successor, e.g. '(ii)',
    appears before the letter after it, e.g. '(j)'.

    :param lines: the parent segment's body lines.
    :param index: the index of the line starting with the candidate marker.
    :param letter: the candidate letter.
    :return: whether the marker is a roman sub-point.
    """
    successor = ROMAN_LETTER_SUCCESSORS.get(letter)
    if not successor:
        return False
    next_letter = f"({chr(ord(letter) + 1)})"
    for line in lines[index + 1:]:
        if line.startswith(f"({successor})"):
            return True
        if line.startswith(next_letter):
            return False
    return False


def extract_points(parent_segment: Segment) -> list[Segment]:
    """
    Get the lettered points, e.g. (a), (b), from a paragraph or annex point.

    Letters must run in sequence, so roman sub-points such as (i) under (b)
    stay inside their point rather than starting a new one. Lines after the
    last point stay with it, as the PDF does not mark where a list ends.

    :param parent_segment: the paragraph or annex point segment.
    :return: a list of point segments, titled with their letter.
    """
    points = []
    expected_letter = "a"
    lines = parent_segment.body

    for index, line in enumerate(lines):
        point_match = RE_POINT.match(line)

        if (point_match and point_match.group(1) == expected_letter
                and not _is_roman_sub_point(lines, index, expected_letter)):
            points.append(Segment(
                type="point",
                id=f"{parent_segment.id}:{expected_letter}",
                num=len(points) + 1,
                title=expected_letter,
                parent_id=parent_segment.id,
                body=[line],
            ))
            expected_letter = chr(ord(expected_letter) + 1)
        elif points:
            points[-1].body.append(line)

    return points


def extract_annex_points(annex_segment: Segment) -> list[Segment]:
    """
    Get the numbered points of an annex, e.g. Annex III point 4.

    Numbers must run in sequence, so stray numbered lines are kept in the
    current point. Annexes whose numbering restarts per section only get
    their first run of points.

    :param annex_segment: the annex segment.
    :return: a list of point segments, titled with their number.
    """
    points = []
    expected_number = 1

    for line in annex_segment.body:
        point_match = RE_ANNEX_POINT.match(line)

        if point_match and int(point_match.group(1)) == expected_number:
            points.append(Segment(
                type="point",
                id=f"{annex_segment.id}:{expected_number}",
                num=expected_number,
                title=str(expected_number),
                parent_id=annex_segment.id,
                body=[line],
            ))
            expected_number += 1
        elif points:
            points[-1].body.append(line)

    return points


def extract_segments(pdf_path: Path) -> list[Segment]:
    """
    Extract all chapter, section, article, paragraph, and annex segments from
    the .PDF file.

    :param pdf_path: the path to the source .PDF file.
    :return: the list of segments in the .PDF file.
    """

    all_lines = read_pdf_lines(pdf_path)
    segments: list[Segment] = []
    current_chapter = None
    current_section = None

    # Three regions: preamble, enacting terms, annexes. Track which we're in
    # so annex cross-references aren't mistaken for new articles.
    in_enacting_terms = False
    in_annexes = False
    i = 0

    while i < len(all_lines):
        line = all_lines[i]

        if line is None or is_footer(line):
            i += 1
            continue

        stripped_line = line.strip()

        # Handle annexes.
        # The annexes follow the enacting terms and run to the end of the
        # file. After the first one, chapters and articles are not parsed.
        annex_match = RE_ANNEX.match(stripped_line)
        if annex_match:
            in_annexes = True
            current_chapter = None
            current_section = None
            annex_roman = annex_match.group(1)
            title_line_index, title = find_title_after_heading(
                all_lines, i + 1
            )

            segments.append(Segment(
                type="annex",
                id=f"annex:{annex_roman}",
                num=ROMAN_TO_INT[annex_roman],
                title=title,
            ))

            i = title_line_index + 1

            continue

        # Everything after the first annex heading is annex body text.
        if in_annexes:
            if segments and stripped_line:
                segments[-1].body.append(stripped_line)
            i += 1
            continue

        chapter_match = RE_CHAPTER.match(stripped_line)

        # Handle chapters.
        # Add a chapter segment.
        if chapter_match:
            in_enacting_terms = True
            chapter_roman = chapter_match.group(1)
            title_line_index, title = find_title_after_heading(
                all_lines, i + 1
            )
            current_chapter = chapter_roman
            current_section = None

            segments.append(Segment(
                type="chapter",
                id=f"ch:{chapter_roman}",
                num=ROMAN_TO_INT[chapter_roman],
                title=title,
            ))

            i = title_line_index + 1

            continue

        # The preamble comes before the first chapter. Its numbered "(N)"
        # recital clauses are context, not provisions, so skip them.
        if not in_enacting_terms:
            i += 1
            continue

        # Handle sections.
        # A section subdivides a chapter and groups its articles. Section
        # numbers restart in each chapter, so qualify the id with the chapter.
        section_match = RE_SECTION.match(stripped_line)
        if section_match:
            section_num = int(section_match.group(1))
            title_line_index, title = find_title_after_heading(
                all_lines, i + 1
            )
            current_section = f"sec:{current_chapter}:{section_num}"

            segments.append(Segment(
                type="section",
                id=current_section,
                num=section_num,
                title=title,
                parent_id=f"ch:{current_chapter}",
            ))

            i = title_line_index + 1

            continue

        # Handle articles.
        # Add an article segment.
        article_match = RE_ARTICLE.match(stripped_line)
        if article_match:
            article_number = article_match.group(1)
            title_line_index, title = find_title_after_heading(
                all_lines, i + 1
            )
            if any(pattern.match(title) for pattern in
                   (RE_ARTICLE, RE_CHAPTER, RE_SECTION, RE_ANNEX)):
                title = ""

            # Articles sit under their section if the chapter has sections,
            # otherwise directly under the chapter.
            parent_id = current_section or (
                f"ch:{current_chapter}" if current_chapter else None
            )

            segments.append(Segment(
                type="article",
                id=f"art:{article_number}",
                num=int(article_number),
                title=title,
                parent_id=parent_id,
            ))

            i = title_line_index + 1

            continue

        if segments and stripped_line:
            segments[-1].body.append(stripped_line)

        i += 1

    # Build the flat list by going over segments and expanding each article
    # into its numbered paragraphs and their lettered points, and each annex
    # into its numbered points and their lettered points.
    expanded_segments: list[Segment] = []

    for segment in segments:
        expanded_segments.append(segment)
        if segment.type == "article":
            for paragraph in extract_paragraphs(segment):
                expanded_segments.append(paragraph)
                expanded_segments.extend(extract_points(paragraph))
        elif segment.type == "annex":
            for annex_point in extract_annex_points(segment):
                expanded_segments.append(annex_point)
                expanded_segments.extend(extract_points(annex_point))

    # Return the flat list of segments.
    # Chapters, sections, articles, paragraphs, annexes, and points.
    return expanded_segments
