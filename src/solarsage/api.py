"""FastAPI service exposing the RAG pipeline."""

from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, HTTPException

from .generate import generate_answer
from .ingest import load_corpus
from .retrieval import TfidfRetriever

DOCS_DIR = Path(__file__).resolve().parents[2] / "data" / "docs"

app = FastAPI(title="SolarSage", version="0.1.0")
_retriever = None


def get_retriever() -> TfidfRetriever:
    global _retriever
    if _retriever is None:
        _retriever = TfidfRetriever(load_corpus(DOCS_DIR))
    return _retriever


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "chunks": len(get_retriever().corpus)}


@app.get("/ask")
def ask(q: str, k: int = 4) -> dict:
    if not q.strip():
        raise HTTPException(status_code=400, detail="empty question")
    results = get_retriever().retrieve(q, k=k)
    response = generate_answer(q, results)
    response["question"] = q
    return response
