import asyncio
from typing import Generator

import pytest
from fastapi.testclient import TestClient
from tortoise.contrib.test import finalizer, initializer

from FotoAgenda.app import app
from FotoAgenda.config.variables import config

DB_URL = "sqlite://:memory:"


@pytest.fixture(scope="session")
def event_loop():
    return asyncio.get_event_loop()


@pytest.fixture(scope="session")
def client() -> Generator:
    initializer(
        db_url=DB_URL,
        modules=config.tortoise_models,
    )

    with TestClient(app) as c:
        yield c

    finalizer()
