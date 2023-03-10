from fastapi.testclient import TestClient

from FotoAgenda.app import app
from FotoAgenda.utils.logger import logger

log = logger()


def test_base_redirect_to_doc(client: TestClient):
    res = client.get("/")
    assert app.docs_url == res.url.path


def test_healthcheck(client: TestClient):
    res = client.get("/healthcheck")
    assert res.json() == {"message": "ok"}
