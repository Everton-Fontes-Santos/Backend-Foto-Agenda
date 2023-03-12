import pytest
from fastapi.exceptions import HTTPException

from FotoAgenda.models.client_model import Client_Pydantic, ClientModel
from FotoAgenda.utils.api.post_items import post_items

pytest_plugins = ("pytest_asyncio",)


@pytest.mark.asyncio
async def test_post_one_item(client):
    @post_items(model=ClientModel, pydantic=Client_Pydantic)
    async def to_decorated(items: list[Client_Pydantic]):
        ...

    lengh = len(await ClientModel.all())
    cli = [
        Client_Pydantic(
            **{
                "id": lengh + 1,
                "first_name": "string",
                "last_name": "string",
                "email": "string",
                "phone": "string",
                "instagram": "string",
                "facebook": "string",
                "cpf": f"{lengh+1}12341541",
            }
        )
    ]
    assert len(await to_decorated(cli)) == 1


@pytest.mark.asyncio
async def test_post_raises_HTTPException(client):
    @post_items(model=ClientModel, pydantic=Client_Pydantic)
    async def to_decorated(items: list[Client_Pydantic]):
        ...

    cli = [
        Client_Pydantic(
            **{
                "id": 2147483647,
                "first_name": "string",
                "last_name": "string",
                "email": "string",
                "phone": "string",
                "instagram": "string",
                "facebook": "string",
                "cpf": "string",
            }
        )
    ]
    with pytest.raises(HTTPException):
        await to_decorated(cli)
