"""Load markdown documents and split them into overlapping chunks."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

DEFAULT_CHUNK_SIZE = 800  # characters
DEFAULT_OVERLAP = 150


@dataclass
class Chunk:
    doc_id: str
    chunk_id: int
    text: str


def chunk_text(text: str, size: int = DEFAULT_CHUNK_SIZE, overlap: int = DEFAULT_OVERLAP) -> list[str]:
    """Split text into overlapping character windows, breaking on whitespace where possible."""
    if size <= overlap:
        raise ValueError("chunk size must be greater than overlap")
    text = text.strip()
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + size, len(text))
        # avoid cutting mid-word: back up to the last whitespace
        if end < len(text):
            last_space = text.rfind(" ", start, end)
            if last_space > start:
                end = last_space
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end >= len(text):
            break
        start = end - overlap
    return chunks


def load_corpus(docs_dir: str | Path) -> list[Chunk]:
    """Read every .md file in docs_dir and return its chunks."""
    docs_dir = Path(docs_dir)
    corpus: list[Chunk] = []
    for path in sorted(docs_dir.glob("*.md")):
        for i, piece in enumerate(chunk_text(path.read_text(encoding="utf-8"))):
            corpus.append(Chunk(doc_id=path.stem, chunk_id=i, text=piece))
    return corpus
