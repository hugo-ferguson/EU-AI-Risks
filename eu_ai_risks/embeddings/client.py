"""
Embedding model wrapper using sentence-transformers.
"""

import torch
from sentence_transformers import SentenceTransformer

from eu_ai_risks.db.session import get_session

# Define the model parameters to use to generate embeddings.
MODEL_NAME = "BAAI/bge-base-en-v1.5"
EMBEDDING_DIMENSIONS = 768


def resolve_device() -> str:
	if torch.cuda.is_available():
		return "cuda"
	if torch.backends.mps.is_available():
		return "mps"
	return "cpu"


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


def requirement_embedding_text(title: str, description: str, input_text: str, processing: str) -> str:
	"""Build the text representation used for Requirement embeddings."""
	return (
		f"Requirement: {title}. "
		f"Description: {description}. "
		f"Input: {input_text}. "
		f"Processing: {processing}."
	)


def fetch_requirement_rows() -> list[dict[str, str]]:
	"""Fetch Requirement nodes from Neo4j for embedding."""
	with get_session() as session:
		return list(session.run(
			"""
			MATCH (n:Requirement)
			RETURN n.title AS title,
				n.description AS description,
				n.input AS input,
				n.processing AS processing
			""",
		))


def create_requirement_embedding_index() -> None:
	"""Create the Requirement vector index if it does not already exist."""
	with get_session() as session:
		session.run(
			f"""
			CREATE VECTOR INDEX requirement_embedding IF NOT EXISTS
			FOR (n:Requirement) ON (n.embedding)
			OPTIONS {{indexConfig: {{
				`vector.dimensions`: {EMBEDDING_DIMENSIONS},
				`vector.similarity_function`: 'cosine'
			}}}}
			""",
		)


def write_requirement_embeddings(rows: list[dict[str, str]], embeddings: list[list[float]]) -> None:
	"""Write Requirement embeddings back to Neo4j."""
	with get_session() as session:
		session.run(
			"""
			UNWIND $rows AS row
			MATCH (n:Requirement {title: row.title})
			SET n.embedding = row.embedding
			""",
			rows=[
				{"title": row["title"], "embedding": embedding}
				for row, embedding in zip(rows, embeddings)
			],
		)


def generate_requirements_embeddings() -> int:
	"""Generate embeddings for Requirement nodes and write them to Neo4j."""
	requirement_rows = fetch_requirement_rows()
	if not requirement_rows:
		return 0

	texts = [
		requirement_embedding_text(
			row["title"],
			row["description"],
			row["input"],
			row["processing"],
		)
		for row in requirement_rows
	]

	print(f"  Generating embeddings for {len(texts)} requirements ...")
	embeddings = embed_batch(texts)
	create_requirement_embedding_index()
	write_requirement_embeddings(requirement_rows, embeddings)

	print(f"  Wrote embeddings for {len(requirement_rows)} Requirement nodes.")
	print("  Created vector index for Requirement.")

	return len(requirement_rows)
