from copy import deepcopy
from fastapi.testclient import TestClient
import pytest
import src.app as app_module


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset the in-memory activity data between tests."""
    original_state = deepcopy(app_module.activities)
    yield
    app_module.activities.clear()
    app_module.activities.update(deepcopy(original_state))


@pytest.fixture
def client():
    return TestClient(app_module.app)
