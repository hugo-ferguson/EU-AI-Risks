"""
Unit tests for driver singleton lifecycle and session context (R18).
"""

from eu_ai_risks.db.session import close_driver, get_driver


def test_driver_singleton(monkeypatch):
    """get_driver() must return the same driver instance across calls."""
    fake_driver_instances = []

    class FakeDriver:
        def __init__(self, uri, auth):
            self.uri = uri
            self.auth = auth
            self.closed = False
            fake_driver_instances.append(self)

        def close(self):
            self.closed = True

    import eu_ai_risks.db.session as session_mod
    monkeypatch.setattr(session_mod, "GraphDatabase", type("GD", (), {"driver": FakeDriver}))
    monkeypatch.setattr(session_mod, "NEO4J_USERNAME", "test_user")
    monkeypatch.setattr(session_mod, "NEO4J_PASSWORD", "test_pass")

    close_driver()
    try:
        driver1 = get_driver()
        driver2 = get_driver()
        assert driver1 is driver2
        assert len(fake_driver_instances) == 1
    finally:
        close_driver()
        assert fake_driver_instances[0].closed
