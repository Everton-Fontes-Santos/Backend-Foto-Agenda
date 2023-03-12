import pytest
from fastapi.exceptions import HTTPException

from FotoAgenda.models.client_model import Client_Pydantic, ClientModel
from FotoAgenda.utils.api.delete_item import delete_item

pytest_plugins = ("pytest_asyncio",)


@pytest.mark.asyncio
async def test_delete_one_item(client):
    @delete_item(model=ClientModel, pydantic=Client_Pydantic)
    async def to_decorated(id: int):
        ...

    lengh = len(await ClientModel.all())
    item = await to_decorated(lengh)
    assert item["message"] == "Deleted"


@pytest.mark.asyncio
async def test_raises_DoesNotExists(client):
    @delete_item(model=ClientModel, pydantic=Client_Pydantic)
    async def to_decorated(id: int):
        ...

    with pytest.raises(HTTPException):
        item = await to_decorated(9000000)
