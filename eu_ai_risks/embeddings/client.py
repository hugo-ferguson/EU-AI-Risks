"""
Embedding model wrapper using sentence-transformers.
"""

from __future__ import annotations

import threading

MODEL_NAME = "BAAI/bge-base-en-v1.5"
EMBEDDING_DIMENSIONS = 768


def resolve_device() -> str:
    try:
        import torch
        if torch.cuda.is_available():
            return "cuda"
        if torch.backends.mps.is_available():
            return "mps"
    except ImportError:
        pass
    return "cpu"


class EmbeddingClient:
    """Thread-safe singleton wrapper around the sentence-transformers model."""

    _instance = None
    _model = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def _get_model(self):
        if self._model is None:
            with self._lock:
                if self._model is None:
                    try:
                        from sentence_transformers import SentenceTransformer
                    except ImportError as exc:
                        raise ImportError(
                            "Generating embeddings requires sentence-transformers and PyTorch. "
                            "Install them via 'pip install sentence-transformers torch'."
                        ) from exc
                    device = resolve_device()
                    self._model = SentenceTransformer(MODEL_NAME, device=device)
        return self._model

    def embed_text(self, text: str) -> list[float]:
        """Embed a single text string."""
        return self._get_model().encode(text).tolist()

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        """Embed a batch of text strings."""
        return self._get_model().encode(texts).tolist()


def embed_text(text: str) -> list[float]:
    """Embed a single text string."""
    return EmbeddingClient().embed_text(text)


def embed_batch(texts: list[str]) -> list[list[float]]:
    """Embed a batch of text strings."""
    return EmbeddingClient().embed_batch(texts)
