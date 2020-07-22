# type: ignore
import pytest
from fastapi.testclient import TestClient
from .test_setup import app, refresh_db

client = TestClient(app)


@pytest.fixture(autouse=True)
def before_each_test():
    refresh_db()


def test_create_principle():
    response = client.post("/agile/principle", json={"content": "test principle"})
    assert response.status_code == 201
    assert response.json() == {
        "data": {"content": "test principle", "id": 1},
        "message": "Principle was successfully added",
    }


def test_update_principle():
    test_create_principle()
    response = client.put("/agile/principle/1", json={"content": "update principle"})
    assert response.status_code == 200
    assert response.json() == {
        "data": {"content": "update principle", "id": 1},
        "message": "Principle was successfully updated",
    }


def test_delete_principle():
    test_create_principle()
    response = client.delete("/agile/principle/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Principle was successfully deleted"}


def test_create_value():
    response = client.post("/agile/value", json={"content": "test value"})
    assert response.status_code == 201
    assert response.json() == {
        "data": {"content": "test value", "id": 1},
        "message": "Value was successfully added",
    }


def test_update_value():
    test_create_value()
    response = client.put("/agile/value/1", json={"content": "update value"})
    assert response.status_code == 200
    assert response.json() == {
        "data": {"content": "update value", "id": 1},
        "message": "Value was successfully updated",
    }


def test_delete_value():
    test_create_value()
    response = client.delete("/agile/value/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Value was successfully deleted"}


def test_get_manifesto():
    test_create_principle()
    test_create_value()
    response = client.get("/agile/manifesto")
    assert response.status_code == 200
    assert response.json() == {
        "principles": [{"content": "test principle", "id": 1}],
        "values": [{"content": "test value", "id": 1}],
    }
