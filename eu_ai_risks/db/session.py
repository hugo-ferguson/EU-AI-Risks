"""
Neo4j driver singleton and session context manager.
"""

import logging
import os
from contextlib import contextmanager

from dotenv import load_dotenv
from neo4j import GraphDatabase

logging.getLogger("neo4j").setLevel(logging.ERROR)

load_dotenv()

NEO4J_URI = os.environ.get("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USERNAME = os.environ.get("NEO4J_USERNAME")
NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD")


@contextmanager
def get_session():
    if not NEO4J_USERNAME or not NEO4J_PASSWORD:
        raise RuntimeError(
            "Neo4j credentials are not configured. Set NEO4J_URI, "
            "NEO4J_USERNAME, and NEO4J_PASSWORD in your environment or .env file."
        )
    with GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD)) as driver:
        with driver.session() as session:
            yield session
