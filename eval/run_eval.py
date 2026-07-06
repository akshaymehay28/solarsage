"""Retrieval evaluation: hit-rate@k over a labelled question set.

A question is a "hit" if any of the top-k retrieved chunks comes from the
labelled relevant document. Run: python -m eval.run_eval
"""

from __future__ import annotations

import json
from pathlib import Path

from solarsage.ingest import load_corpus
from solarsage.retrieval import TfidfRetriever

ROOT = Path(__file__).resolve().parents[1]


def main(k_values: tuple[int, ...] = (1, 3, 5)) -> None:
    questions = json.loads((ROOT / "eval" / "questions.json").read_text())
    retriever = TfidfRetriever(load_corpus(ROOT / "data" / "docs"))

    print(f"Corpus: {len(retriever.corpus)} chunks | Questions: {len(questions)}\n")
    for k in k_values:
        hits = 0
        for item in questions:
            results = retriever.retrieve(item["question"], k=k)
            if any(r.chunk.doc_id == item["relevant_doc"] for r in results):
                hits += 1
        print(f"hit-rate@{k}: {hits / len(questions):.2%} ({hits}/{len(questions)})")


if __name__ == "__main__":
    main()
