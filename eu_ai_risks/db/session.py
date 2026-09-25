"""
Neo4j driver singleton and session context manager.
"""

from __future__ import annotations

import atexit
import logging
import os
import threading
from contextlib import contextmanager

from dotenv import load_dotenv
from neo4j import Driver, GraphDatabase

logging.getLogger("neo4j").setLevel(logging.ERROR)

load_dotenv()

NEO4J_URI = os.environ.get("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USERNAME = os.environ.get("NEO4J_USERNAME")
NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD")

_driver: Driver | None = None
_lock = threading.Lock()


def get_driver() -> Driver:
    """Return the shared application-scoped Neo4j driver singleton."""
    global _driver
    if _driver is None:
        with _lock:
            if _driver is None:
                if not NEO4J_USERNAME or not NEO4J_PASSWORD:
                    raise RuntimeError(
                        "Neo4j credentials are not configured. Set NEO4J_URI, "
                        "NEO4J_USERNAME, and NEO4J_PASSWORD in your environment or .env file."
                    )
                _driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))
    return _driver


def close_driver() -> None:
    """Close the shared driver singleton on application shutdown."""
    global _driver
    with _lock:
        if _driver is not None:
            _driver.close()
            _driver = None


atexit.register(close_driver)


@contextmanager
def get_session():
    """Yield a short-lived session from the shared driver connection pool."""
    driver = get_driver()
    with driver.session() as session:
        yield session
