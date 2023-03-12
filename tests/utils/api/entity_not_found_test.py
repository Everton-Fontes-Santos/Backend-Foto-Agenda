import pytest

from FotoAgenda.models.client_model import Client_Pydantic, ClientModel
from FotoAgenda.utils.api.not_found_entity import (
    DoesNotExist,
    HTTPException,
    entity_not_found,
)

pytest_plugins = ("pytest_asyncio",)


@pytest.mark.asyncio
async def test_raises_http_Exception(client):
    @entity_not_found
    async def to_decorated(id: int):
        res = await Client_Pydantic.from_queryset(ClientModel.filter(id=id))
        if res:
            return res
        raise DoesNotExist()

    with pytest.raises(HTTPException):
        id = 90000
        await to_decorated(id)


@pytest.mark.asyncio
async def test_not_raises_http_Exception(client):
    @entity_not_found
    async def to_decorated(id: int):
        res = await Client_Pydantic.from_queryset(ClientModel.filter(id=id))
        if res:
            return res
        raise DoesNotExist()

    try:
        id = 1
        await to_decorated(id)
        assert True
    except HTTPException:
        assert False
