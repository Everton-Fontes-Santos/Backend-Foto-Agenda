import pytest

from FotoAgenda.models.client_model import Client_Pydantic, ClientModel
from FotoAgenda.utils.api.get_by_id import DoesNotExist, get_by_id

pytest_plugins = ("pytest_asyncio",)


@pytest.mark.asyncio
async def test_return_one_item(client):
    @get_by_id(model=ClientModel, pydantic=Client_Pydantic)
    async def to_decorated(id: int):
        ...

    item = await to_decorated(1)
    assert type((item, Client_Pydantic))


@pytest.mark.asyncio
async def test_raises_DoesNotExists(client):
    @get_by_id(model=ClientModel, pydantic=Client_Pydantic)
    async def to_decorated(id: int):
        ...

    with pytest.raises(DoesNotExist):
        item = await to_decorated(9000000)
