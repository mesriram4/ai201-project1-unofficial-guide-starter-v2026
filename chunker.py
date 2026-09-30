"""
Stage 2 of the pipeline: splitting documents into chunks.

⚠️ THIS IS THE FILE YOU CHANGE IN MILESTONE 3.

`split_documents` below is deliberately plain. It cuts every document into
fixed-size pieces with a fixed overlap and pays no attention to where sentences
or paragraphs end. It works, and it is not good.

On a corpus of short posts it may not cut anything at all: `campus_life` comes
out as 88 documents and 88 chunks, because almost nothing in it reaches 800
characters. That is the baseline, not a bug — Milestone 3 is where you decide
whether one post should stay one chunk.

Your job in Milestone 3 is to replace the *body* of `split_documents` with a
strategy that fits the documents you actually read in Milestone 1. Keep the
name and the shape of what it returns — the rest of the pipeline calls it, and
your README has to name the function that produced your chunks.

If you get stuck for 30 minutes, `fallback_split` is the original. Switch back
to it, write down what you saw, and move on. That's a real observation about
your pipeline, not giving up.
"""

import re
from dataclasses import dataclass

import config
from ingest import Document


@dataclass
class Chunk:
    """One piece of one document."""

    text: str
    source: str        # which file it came from
    index: int         # which chunk within that file, starting at 0
    produced_by: str   # the function that made it — cite this in your README

    @property
    def label(self) -> str:
        return f"{self.source}#{self.index}"


def fallback_split(
    documents: list[Document],
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[Chunk]:
    """
    The starter's original chunker. Fixed-size character windows with overlap.

    Keep this function. Milestone 3's stop rule points back at it, and having
    something to compare your own strategy against is useful in unit 2.
    """
    chunk_size = chunk_size or config.CHUNK_SIZE
    overlap = overlap or config.CHUNK_OVERLAP

    if overlap >= chunk_size:
        raise ValueError("overlap has to be smaller than chunk_size")

    chunks: list[Chunk] = []
    for doc in documents:
        start = 0
        index = 0
        while start < len(doc.text):
            piece = doc.text[start : start + chunk_size].strip()
            if piece:
                chunks.append(
                    Chunk(
                        text=piece,
                        source=doc.source,
                        index=index,
                        produced_by="chunker.py::fallback_split",
                    )
                )
                index += 1
            start += chunk_size - overlap

    return chunks


_HEADING_RE = re.compile(r"(?m)^(#{1,6}\s+.*)$")
_PARAGRAPH_RE = re.compile(r"\n\s*\n")
_SENTENCE_RE = re.compile(r"(?<=\.)\s+")


def _sections(text: str) -> list[tuple[str | None, str]]:
    """Split a document's text into (heading, body) pairs on '#'/'##' lines."""
    parts = _HEADING_RE.split(text)

    sections: list[tuple[str | None, str]] = []
    if parts[0].strip():
        sections.append((None, parts[0]))
    for i in range(1, len(parts), 2):
        heading = parts[i].strip()
        body = parts[i + 1] if i + 1 < len(parts) else ""
        sections.append((heading, body))
    return sections


def _paragraphs(heading: str | None, body: str) -> list[str]:
    """Paragraphs of one section, with the heading folded into the first."""
    paragraphs = [p.strip() for p in _PARAGRAPH_RE.split(body) if p.strip()]
    if heading:
        if paragraphs:
            paragraphs[0] = f"{heading}\n\n{paragraphs[0]}"
        else:
            paragraphs = [heading]
    return paragraphs


def _sentence_groups(sentences: list[str], group_size: int) -> list[list[str]]:
    """Sentences grouped by threes, with a short tail folded into the group before it."""
    groups = [
        sentences[i : i + group_size] for i in range(0, len(sentences), group_size)
    ]
    if len(groups) > 1 and len(groups[-1]) < group_size:
        groups[-2].extend(groups.pop())
    return groups


def split_documents(documents: list[Document]) -> list[Chunk]:
    """
    Split documents section by section, paragraph by paragraph, into groups
    of three sentences (on periods).

    A period is where the writer ended one thought and started the next, so
    grouping three of them gives each chunk a little more context than a
    single sentence alone, while still cutting on real sentence boundaries.

    The three-sentence grouping resets at every paragraph break, and
    paragraphs are scoped to the section they fall under ('#'/'##' headings).
    Without that, a group of three could straddle a paragraph or section
    boundary and glue two unrelated ideas into one chunk — e.g. the last
    sentence of a "Practical" section opening followed by the first two
    sentences of the next town's paragraph.

    A paragraph that doesn't divide evenly by three no longer leaves its
    remainder as its own tiny, context-free chunk (a lone "The pump room and
    gardens are level throughout." with no town name in it). Instead the
    remainder is folded into the group before it, within the same paragraph.
    If the whole paragraph is shorter than three sentences to begin with —
    so there's no earlier group in it to fold into — it's folded onto the
    previous chunk instead, as long as that chunk is still in the same
    section; a short paragraph that opens a brand-new section stands on its
    own rather than borrowing from the section before it.

    No length guard here on purpose: `config.CHUNK_SIZE` is tuned for a
    single sentence, and windowing a 3-sentence group down to that size was
    cutting chunks off mid-group instead of leaving them three sentences
    long. Folding remainders in means most chunks run three to five
    sentences rather than every chunk being at risk of truncation.

    Note: this only splits on periods, not "!" or "?" — a sentence ending in
    either of those gets folded into whatever follows it, up to the next
    period, before the three-sentence grouping happens.
    """
    group_size = 3

    chunks: list[Chunk] = []
    for doc in documents:
        doc_chunks: list[Chunk] = []

        for heading, body in _sections(doc.text):
            section_start = len(doc_chunks)

            for paragraph in _paragraphs(heading, body):
                sentences = [
                    s.strip() for s in _SENTENCE_RE.split(paragraph) if s.strip()
                ]
                if not sentences:
                    continue

                groups = _sentence_groups(sentences, group_size)

                if (
                    len(groups) == 1
                    and len(groups[0]) < group_size
                    and len(doc_chunks) > section_start
                ):
                    doc_chunks[-1].text += " " + " ".join(groups[0])
                    continue

                for group in groups:
                    doc_chunks.append(
                        Chunk(
                            text=" ".join(group),
                            source=doc.source,
                            index=len(doc_chunks),
                            produced_by="chunker.py::split_documents",
                        )
                    )

        chunks.extend(doc_chunks)

    return chunks


def describe(chunks: list[Chunk]) -> str:
    """A one-line summary, printed after indexing."""
    if not chunks:
        return "0 chunks"
    lengths = [len(c.text) for c in chunks]
    return (
        f"{len(chunks)} chunks, "
        f"{sum(lengths) // len(lengths)} characters on average "
        f"(shortest {min(lengths)}, longest {max(lengths)}), "
        f"produced by {chunks[0].produced_by}"
    )


if __name__ == "__main__":
    from ingest import load_documents

    chunks = split_documents(load_documents())
    print(describe(chunks))
