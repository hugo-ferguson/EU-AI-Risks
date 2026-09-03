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
    # into its numbered paragraphs.
    segments_with_paragraphs: list[Segment] = []

    # For each segment, if it is an article, extract its paragraphs from its
    # body.
    for segment in segments:
        segments_with_paragraphs.append(segment)
        if segment.type == "article":
            segments_with_paragraphs.extend(extract_paragraphs(segment))

    # Return the flat list of segments.
    # Chapters, sections, articles, paragraphs, and annexes.
    return segments_with_paragraphs
