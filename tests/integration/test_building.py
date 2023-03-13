from fastapi.testclient import TestClient

import models
from core.config import settings


def test_get_buildings(client: TestClient, buildings):
    response = client.get(f"{settings.API_STR}/buildings")

    assert response.status_code == 200
    data = response.json()

    assert data
    assert len(data) == len(buildings)
    assert set(data[0].keys()) == {"id", "name", "address", "owner"}


def test_create_building(client: TestClient):
    create_data = {"name": "My Building", "address": "The Street no. 1", "owner": "Mr. Nielsen"}
    response = client.post(f"{settings.API_STR}/buildings", json=create_data)

    assert response.status_code == 201
    data = response.json()

    assert data
    del data["id"]
    assert data == create_data


def test_update_building(client: TestClient, buildings):
    data = {"name": "New Name"}
    response = client.put(f"{settings.API_STR}/buildings/{buildings[0].id}", json=data)

    assert response.status_code == 200
    data = response.json()

    assert data
    assert data["name"] == "New Name"


def test_delete_building(client: TestClient, buildings):
    response = client.delete(f"{settings.API_STR}/buildings/{buildings[0].id}")

    assert response.status_code == 200

    assert len(models.Building.find_all().to_list()) == len(buildings) - 1
