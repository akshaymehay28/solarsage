"""Retrieval over document chunks: three interchangeable strategies.

- TfidfRetriever: sparse lexical matching (baseline)
- LsaRetriever: dense semantic vectors via truncated SVD over TF-IDF (LSA),
  which can match on meaning when the query and document use different words
- HybridRetriever: weighted score fusion of the two

All three share the same interface so they can be swapped in the API and
compared head-to-head in eval/run_eval.py.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import Normalizer

from .ingest import Chunk


@dataclass
class RetrievedChunk:
    chunk: Chunk
    score: float


class BaseRetriever:
    name = "base"

    def __init__(self, corpus: list[Chunk]):
        if not corpus:
            raise ValueError("corpus is empty")
        self.corpus = corpus

    def _scores(self, query: str) -> np.ndarray:  # pragma: no cover - abstract
        raise NotImplementedError

    def retrieve(self, query: str, k: int = 4) -> list[RetrievedChunk]:
        scores = self._scores(query)
        top = np.argsort(scores)[::-1][:k]
        return [RetrievedChunk(chunk=self.corpus[i], score=float(scores[i])) for i in top]


class TfidfRetriever(BaseRetriever):
    """Sparse lexical retrieval. Fast, transparent, strong when the query
    reuses the document's vocabulary."""

    name = "tfidf"

    def __init__(self, corpus: list[Chunk]):
        super().__init__(corpus)
        self.vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
        self.matrix = self.vectorizer.fit_transform(c.text for c in corpus)

    def _scores(self, query: str) -> np.ndarray:
        query_vec = self.vectorizer.transform([query])
        return cosine_similarity(query_vec, self.matrix).ravel()


class LsaRetriever(BaseRetriever):
    """Dense semantic retrieval: TF-IDF reduced to a low-rank latent space
    (latent semantic analysis). Terms that co-occur across the corpus land
    near each other, so "dirt on panels" can match a soiling document even
    without shared keywords."""

    name = "lsa"

    def __init__(self, corpus: list[Chunk], n_components: int = 128):
        super().__init__(corpus)
        self.vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
        tfidf = self.vectorizer.fit_transform(c.text for c in corpus)
        n_components = min(n_components, tfidf.shape[0] - 1, tfidf.shape[1] - 1)
        self.svd = TruncatedSVD(n_components=n_components, random_state=0)
        self.normalizer = Normalizer(copy=False)
        self.matrix = self.normalizer.fit_transform(self.svd.fit_transform(tfidf))

    def _scores(self, query: str) -> np.ndarray:
        query_vec = self.normalizer.transform(
            self.svd.transform(self.vectorizer.transform([query]))
        )
        return cosine_similarity(query_vec, self.matrix).ravel()


class HybridRetriever(BaseRetriever):
    """Weighted fusion of lexical and semantic scores. alpha=1.0 is pure
    TF-IDF, alpha=0.0 is pure LSA."""

    name = "hybrid"

    def __init__(self, corpus: list[Chunk], alpha: float = 0.5):
        super().__init__(corpus)
        self.alpha = alpha
        self.tfidf = TfidfRetriever(corpus)
        self.lsa = LsaRetriever(corpus)

    def _scores(self, query: str) -> np.ndarray:
        return self.alpha * self.tfidf._scores(query) + (1 - self.alpha) * self.lsa._scores(query)


RETRIEVERS = {r.name: r for r in (TfidfRetriever, LsaRetriever, HybridRetriever)}


def make_retriever(name: str, corpus: list[Chunk]) -> BaseRetriever:
    if name not in RETRIEVERS:
        raise ValueError(f"unknown retriever '{name}', choose from {sorted(RETRIEVERS)}")
    return RETRIEVERS[name](corpus)
