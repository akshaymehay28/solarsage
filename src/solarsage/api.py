"""FastAPI service exposing the RAG pipeline.

Set RETRIEVER=tfidf|lsa|hybrid to choose the retrieval strategy
(default: hybrid).
"""

from __future__ import annotations

import os
from pathlib import Path

from fastapi import FastAPI, HTTPException

from .generate import generate_answer
from .ingest import load_corpus
from .retrieval import BaseRetriever, make_retriever

DOCS_DIR = Path(__file__).resolve().parents[2] / "data" / "docs"

app = FastAPI(title="SolarSage", version="0.2.0")
_retriever: BaseRetriever | None = None


def get_retriever() -> BaseRetriever:
    global _retriever
    if _retriever is None:
        name = os.environ.get("RETRIEVER", "hybrid")
        _retriever = make_retriever(name, load_corpus(DOCS_DIR))
    return _retriever


@app.get("/health")
def health() -> dict:
    r = get_retriever()
    return {"status": "ok", "chunks": len(r.corpus), "retriever": r.name}


@app.get("/ask")
def ask(q: str, k: int = 4) -> dict:
    if not q.strip():
        raise HTTPException(status_code=400, detail="empty question")
    results = get_retriever().retrieve(q, k=k)
    response = generate_answer(q, results)
    response["question"] = q
    response["retriever"] = get_retriever().name
    return response
