import pytest

from fastapi.testclient import TestClient
from unittest.mock import Mock

from ...app.controllers.property_controller import PropertyController
from ...app.controllers.status_controller import StatusController
from ...app.controllers.status_history_controller import StatusHistoryController
from ...app.controllers.search_controller import SearchController
from ...app.routes.endpoints import router
from ...app.utils.SearchRequest_example import example_search_request_filters


@pytest.fixture
def app():
    yield router


@pytest.fixture
def client(app):
    with TestClient(app) as client:
        yield client


# ------------------------------------ TESTS PROPERTY ------------------------------------


def test_get_properties_success(client, monkeypatch):
    mock_get_properties = Mock(return_value=[{"id": 1, "address": "calle 123", "city": "City", "price": 100000}])
    monkeypatch.setattr(PropertyController, "get_properties", mock_get_properties)

    response = client.get("/properties")

    assert response.status_code == 200
    assert response.json() == {
        "properties": mock_get_properties.return_value,
        "message": "Properties retrieved",
        "status": 200,
    }


def test_get_properties_no_data(client, monkeypatch):
    mock_get_empty_properties = Mock(return_value=[])
    monkeypatch.setattr(PropertyController, "get_properties", mock_get_empty_properties)

    response = client.get("/properties")

    assert response.status_code == 200
    assert response.json() == {
        "properties": [],
        "message": "No data found",
        "status": 200,
    }


def test_get_properties_error(client, monkeypatch):
    monkeypatch.setattr(PropertyController, "get_properties", lambda: Exception("Exception message goes here"))

    with pytest.raises(Exception):
        response = client.get("/properties")


def test_get_properties_success(client, monkeypatch):
    mock_get_properties = Mock(return_value=[{"id": 1, "address": "calle 123", "city": "City", "price": 100000}])
    monkeypatch.setattr(PropertyController, "get_properties", mock_get_properties)

    response = client.get("/properties")

    assert response.status_code == 200
    assert response.json() == {
        "properties": mock_get_properties.return_value,
        "message": "Properties retrieved",
        "status": 200,
    }


def test_get_properties_no_data(client, monkeypatch):
    mock_get_empty_properties = Mock(return_value=[])
    monkeypatch.setattr(PropertyController, "get_properties", mock_get_empty_properties)

    response = client.get("/properties")

    assert response.status_code == 200
    assert response.json() == {
        "properties": [],
        "message": "No data found",
        "status": 200,
    }


def test_get_properties_error(client, monkeypatch):
    monkeypatch.setattr(PropertyController, "get_properties", lambda: Exception("Exception message goes here"))

    with pytest.raises(Exception):
        response = client.get("/properties")


# ------------------------------------ TESTS STATUS ------------------------------------


def test_get_status_success(client, monkeypatch):
    mock_get_status = Mock(return_value=[{"id": 1, "name": "comprando", "label": "Inmueble en proceso de compra"}])
    monkeypatch.setattr(StatusController, "get_status", mock_get_status)

    response = client.get("/status")

    assert response.status_code == 200
    assert response.json() == {
        "status_list": mock_get_status.return_value,
        "message": "Status retrieved",
        "status": 200,
    }


def test_get_status_no_data(client, monkeypatch):
    mock_get_empty_status = Mock(return_value=[])
    monkeypatch.setattr(StatusController, "get_status", mock_get_empty_status)

    response = client.get("/status")

    assert response.status_code == 200
    assert response.json() == {
        "status_list": [],
        "message": "No data found",
        "status": 200,
    }


def test_get_status_error(client, monkeypatch):
    monkeypatch.setattr(StatusController, "get_status", lambda: Exception("Exception message goes here"))

    with pytest.raises(Exception):
        response = client.get("/status")


# ------------------------------------ TESTS STATUS_HISTORY ------------------------------------


def test_get_status_history_success(client, monkeypatch):
    mock_get_status_history = Mock(
        return_value=[{"id": 1, "property_id": 1, "status_id": 1, "update_date": "2021-04-10"}]
    )
    monkeypatch.setattr(StatusHistoryController, "get_status_history", mock_get_status_history)

    response = client.get("/status_history")

    assert response.status_code == 200
    assert response.json() == {
        "status_histories": mock_get_status_history.return_value,
        "message": "Status_histories retrieved",
        "status": 200,
    }


def test_get_status_history_no_data(client, monkeypatch):
    mock_get_empty_status_history = Mock(return_value=[])
    monkeypatch.setattr(StatusHistoryController, "get_status_history", mock_get_empty_status_history)

    response = client.get("/status_history")

    assert response.status_code == 200
    assert response.json() == {
        "status_histories": [],
        "message": "No data found",
        "status": 200,
    }


def test_get_status_history_error(client, monkeypatch):
    monkeypatch.setattr(
        StatusHistoryController, "get_status_history", lambda: Exception("Exception message goes here")
    )

    with pytest.raises(Exception):
        response = client.get("/status_history")


# ------------------------------------ TESTS SEARCH ------------------------------------


def test_search_data_success(client, monkeypatch):
    mock_get_search = Mock(return_value=[{"id": 1, "address": "123 Main St", "city": "Example City"}])
    monkeypatch.setattr(SearchController, "get_search", mock_get_search)

    response = client.post("/search", json=example_search_request_filters)

    assert response.status_code == 200
    assert response.json() == {
        "data": mock_get_search.return_value,
        "message": "Data retrieved",
        "status": 200,
    }


def test_search_data_failure(client, monkeypatch):
    monkeypatch.setattr(SearchController, "get_search", lambda: Exception("Exception message goes here"))

    with pytest.raises(Exception):
        response = client.post("/search", json={})
