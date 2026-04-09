"""
Embedding model wrapper using sentence-transformers.
"""

from sentence_transformers import SentenceTransformer

# Define the model parameters to use to generate embeddings.
MODEL_NAME = "BAAI/bge-base-en-v1.5"
EMBEDDING_DIMENSIONS = 768


class EmbeddingClient:
	"""Singleton wrapper around the sentence-transformers model."""

	_instance = None
	_model: SentenceTransformer | None = None

	def __new__(cls):
		if cls._instance is None:
			cls._instance = super().__new__(cls)
		return cls._instance

	def _get_model(self) -> SentenceTransformer:
		if self._model is None:
			self._model = SentenceTransformer(MODEL_NAME)
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
