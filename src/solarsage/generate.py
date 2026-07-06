"""Answer generation: LLM if an API key is available, extractive fallback otherwise."""

from __future__ import annotations

import os

from .retrieval import RetrievedChunk

SYSTEM_PROMPT = (
    "You are SolarSage, an assistant for solar PV operations and maintenance. "
    "Answer ONLY from the provided context. If the context does not contain "
    "the answer, say so plainly. Cite the doc_id of each source you use."
)


def _format_context(results: list[RetrievedChunk]) -> str:
    return "\n\n".join(f"[{r.chunk.doc_id}#{r.chunk.chunk_id}] {r.chunk.text}" for r in results)


def generate_answer(question: str, results: list[RetrievedChunk]) -> dict:
    """Return {'answer': str, 'sources': [...], 'mode': 'llm'|'extractive'}."""
    sources = [f"{r.chunk.doc_id}#{r.chunk.chunk_id}" for r in results]

    if os.environ.get("ANTHROPIC_API_KEY"):
        import anthropic  # imported lazily so the package is optional

        client = anthropic.Anthropic()
        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=600,
            system=SYSTEM_PROMPT,
            messages=[{
                "role": "user",
                "content": f"Context:\n{_format_context(results)}\n\nQuestion: {question}",
            }],
        )
        return {"answer": message.content[0].text, "sources": sources, "mode": "llm"}

    # Extractive fallback: return the most relevant passages verbatim.
    best = results[:2]
    answer = "Most relevant passages found:\n\n" + "\n\n".join(
        f"({r.chunk.doc_id}) {r.chunk.text}" for r in best
    )
    return {"answer": answer, "sources": sources, "mode": "extractive"}
