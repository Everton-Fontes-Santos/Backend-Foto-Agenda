from fastapi.testclient import TestClient

from FotoAgenda.app import app
from FotoAgenda.utils.logger import logger

log = logger()
client = TestClient(app)


def test_base_redirect_to_doc():
    res = client.get("/")
    assert app.docs_url == res.url.path


def test_healthcheck():
    res = client.get("/healthcheck")
    assert res.json() == {"message": "ok"}
