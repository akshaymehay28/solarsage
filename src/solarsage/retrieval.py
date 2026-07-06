"""TF-IDF retrieval over document chunks.

A deliberate, measurable baseline. Swap in embedding retrieval later and
compare both with eval/run_eval.py.
"""

from __future__ import annotations

from dataclasses import dataclass

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .ingest import Chunk


@dataclass
class RetrievedChunk:
    chunk: Chunk
    score: float


class TfidfRetriever:
    def __init__(self, corpus: list[Chunk]):
        if not corpus:
            raise ValueError("corpus is empty")
        self.corpus = corpus
        self.vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
        self.matrix = self.vectorizer.fit_transform(c.text for c in corpus)

    def retrieve(self, query: str, k: int = 4) -> list[RetrievedChunk]:
        query_vec = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vec, self.matrix).ravel()
        top = scores.argsort()[::-1][:k]
        return [RetrievedChunk(chunk=self.corpus[i], score=float(scores[i])) for i in top]
