import pytest

from FotoAgenda.models.client_model import Client_Pydantic, ClientModel
from FotoAgenda.utils.api.get_all import get_all_itens

pytest_plugins = ("pytest_asyncio",)


@pytest.mark.asyncio
async def test_return_list(client):
    @get_all_itens(model=ClientModel, pydantic=Client_Pydantic)
    async def to_decorated():
        ...

    assert len(await to_decorated()) == 1
