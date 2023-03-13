import time
from typing import Generator

import docker
import pytest
from fastapi.testclient import TestClient

from core.config import settings
from core.connection import create_mongo_client


@pytest.fixture(scope="session")
def docker_client():
    yield docker.from_env()


@pytest.fixture(scope="session")
def mongodb(docker_client):
    container = docker_client.containers.run(
        "mongo:6",
        ports={"27017": settings.DATABASE_PORT},
        environment={
            "MONGO_INITDB_ROOT_USERNAME": settings.DATABASE_USER,
            "MONGO_INITDB_ROOT_PASSWORD": settings.DATABASE_PASSWORD,
        },
        detach=True,
        auto_remove=True,
    )

    time.sleep(3)
    try:
        yield container
    finally:
        container.stop()


@pytest.fixture
def database(mongodb):
    yield
    client = create_mongo_client()
    client.drop_database(settings.DATABASE_NAME)


@pytest.fixture
def client(database) -> Generator:
    from main import app

    with TestClient(app=app, base_url=settings.SERVER_HOST) as _client:
        try:
            yield _client
        except Exception as exc:
            print(exc)
