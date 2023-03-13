import pytest

from models import Building


@pytest.fixture()
def buildings(database):
    buildings = [Building(name=f"Building #{i}", address=f"Street no. {i}", owner=f"Mr. {i}") for i in range(3)]
    Building.insert_many(buildings)

    yield buildings
