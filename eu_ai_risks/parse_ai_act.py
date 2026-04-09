"""
The idea of this script is to break the EU AI Act .PDF file into pieces.
	These are called 'segments' in the code, and contain some metadata about
	them.
The segmented AI Act can then be loaded into a graph using the segments types.
"""

import os
import re
from dataclasses import dataclass, field
from pathlib import Path

import pdfplumber
from dotenv import load_dotenv

load_dotenv()

RE_CHAPTER = re.compile(r'^CHAPTER ([IVX]+)$')
RE_ARTICLE = re.compile(r'^Article (\d+)$')
RE_PARAGRAPH = re.compile(r'^(\d+)\.\s')
RE_FOOTER = re.compile(r'^(EN\s*$|OJ L,|ELI:|/144)')

ROMAN_TO_INT = {
	"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5,
	"VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10,
	"XI": 11, "XII": 12, "XIII": 13,
}


@dataclass
class Segment:
	"""
	type: chapter/article/paragraph
	id: a unique identifier
	num: the chapter/article/paragraph number from the Act
	title: the chapter/article title (paragraphs aren't titled)
	parent_id: the id of the parent node (chapter or article id)
	body: the text following the title of a chapter/article, or a paragraph's
		text.
	"""

	type: str
	id: str
	num: int
	title: str | None = None
	body: list[str] = field(default_factory=list)
	parent_id: str | None = None


def _read_pdf_lines(pdf_path: Path) -> list[str | None]:
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


def _is_footer(line: str) -> bool:
	"""
	Check whether a line is a page footer.

	:param line: the line of text to check.
	:return: whether the line is a footer (these can usually be ignored).
	"""
	return bool(RE_FOOTER.search(line))


def _find_title_after_heading(
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

		# None lines are page breaks, so ignore those.
		# Footers will never contain titles, so ignore those too.
		if line is not None and line.strip() and not _is_footer(line):
			return i, line.strip()

	return heading_index, ""


def _extract_paragraphs(article_segment: Segment) -> list[Segment]:
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

	paragraphs = []

	# Iterate over lines in the article to gather the lines into paragraphs.
	for i, line in enumerate(article_segment.body):
		# Check whether this line is the start of a numbered paragraph.
		paragraph_match = RE_PARAGRAPH.match(line)

		if not paragraph_match:
			continue

		# If it is, save it as the number..
		paragraph_num = int(paragraph_match.group(1))
		paragraph_lines = [line]

		# Gather the following lines until we hit another numbered one.
		# If so, break and collect into the paragraph segment.
		for following_line in article_segment.body[i + 1:]:
			if RE_PARAGRAPH.match(following_line):
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
	Extract all chapter, article, and paragraph segments from the .PDF file.

	:param pdf_path: the path to the source .PDF file.
	:return: the list of segments in the .PDF file.
	"""

	all_lines = _read_pdf_lines(pdf_path)
	segments: list[Segment] = []
	current_chapter = None

	# Start at the first line.
	# Lines can be skipped if they are not useful.
	i = 0

	# Iterate over lines.
	while i < len(all_lines):
		line = all_lines[i]

		# Skip empty (page break) or footer lines.
		if line is None or _is_footer(line):
			i += 1
			continue

		stripped_line = line.strip()

		chapter_match = RE_CHAPTER.match(stripped_line)

		# Handle chapters.
		# Add a chapter segment.
		if chapter_match:
			chapter_roman = chapter_match.group(1)
			title_line_index, title = _find_title_after_heading(
				all_lines, i + 1
			)
			current_chapter = chapter_roman

			segments.append(Segment(
				type="chapter",
				id=f"ch:{chapter_roman}",
				num=ROMAN_TO_INT[chapter_roman],
				title=title,
			))

			i = title_line_index + 1

			continue

		# Handle articles.
		# Add an article segment.
		article_match = RE_ARTICLE.match(stripped_line)
		if article_match:
			article_number = article_match.group(1)
			title_line_index, title = _find_title_after_heading(
				all_lines, i + 1
			)
			if RE_ARTICLE.match(title) or RE_CHAPTER.match(title):
				title = ""
			segments.append(Segment(
				type="article",
				id=f"art:{article_number}",
				num=int(article_number),
				title=title,
				parent_id=f"ch:{current_chapter}" if current_chapter else None,
			))

			i = title_line_index + 1

			continue

		if segments and stripped_line and not _is_footer(stripped_line):
			segments[-1].body.append(stripped_line)

		i += 1

	# Build the flat list by going over chapters and articles and storing the
	# paragraphs.
	segments_with_paragraphs: list[Segment] = []

	# For each segment, if it is an article, extract its paragraphs from its
	# body.
	for segment in segments:
		segments_with_paragraphs.append(segment)
		if segment.type == "article":
			segments_with_paragraphs.extend(_extract_paragraphs(segment))

	# Return the flat list of segments.
	# Chapters, articles, and paragraphs.
	return segments_with_paragraphs


if __name__ == "__main__":
	pdf_path = Path(os.environ["PDF_PATH"])
	print(f"Parsing {pdf_path} ...")
	segments = extract_segments(pdf_path)

	chapters = [seg for seg in segments if seg.type == "chapter"]
	articles = [seg for seg in segments if seg.type == "article"]
	paragraphs = [seg for seg in segments if seg.type == "paragraph"]
	print(f"Found {len(chapters)} chapters, {len(articles)} articles, {len(paragraphs)} paragraphs.\n")

	for chapter in chapters:
		article_count = sum(1 for article in articles if article.parent_id == chapter.id)
		print(f"  {chapter.id}: {chapter.title}  [{article_count} articles]")
