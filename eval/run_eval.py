"""Retrieval evaluation: hit-rate@k per retriever over a labelled question set.

A question is a "hit" if any of the top-k retrieved chunks comes from the
labelled relevant document. Run: PYTHONPATH=src python -m eval.run_eval
"""

from __future__ import annotations

import json
from pathlib import Path

from solarsage.ingest import load_corpus
from solarsage.retrieval import RETRIEVERS

ROOT = Path(__file__).resolve().parents[1]


def hit_rate(retriever, questions, k: int) -> float:
    hits = sum(
        any(r.chunk.doc_id == item["relevant_doc"] for r in retriever.retrieve(item["question"], k=k))
        for item in questions
    )
    return hits / len(questions)


def main(k_values: tuple[int, ...] = (1, 3, 5)) -> None:
    questions = json.loads((ROOT / "eval" / "questions.json").read_text())
    corpus = load_corpus(ROOT / "data" / "docs")
    print(f"Corpus: {len(corpus)} chunks from {len({c.doc_id for c in corpus})} docs | "
          f"Questions: {len(questions)}\n")

    header = "retriever  " + "".join(f"hit@{k:<6}" for k in k_values)
    print(header)
    print("-" * len(header))
    for name, cls in RETRIEVERS.items():
        retriever = cls(corpus)
        row = f"{name:<11}"
        for k in k_values:
            row += f"{hit_rate(retriever, questions, k):<10.1%}"
        print(row)


if __name__ == "__main__":
    main()
