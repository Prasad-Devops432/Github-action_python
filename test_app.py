import pytest
from app import app, read_requirements


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello" in response.data


def test_read_requirements():
    requirements = read_requirements("requirements.txt")
    assert isinstance(requirements, list)
    assert "flask" in requirements