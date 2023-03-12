import pytest
from fastapi.exceptions import HTTPException

from FotoAgenda.models.client_model import Client_Pydantic, ClientModel
from FotoAgenda.utils.api.patch_item import patch_items

pytest_plugins = ("pytest_asyncio",)


@pytest.mark.asyncio
async def test_patch_one_item(client):
    @patch_items(model=ClientModel, pydantic=Client_Pydantic)
    async def to_decorated(item: Client_Pydantic):
        ...

    payload = {
        "id": 1,
        "first_name": "Everton",
        "last_name": "string",
        "email": "string",
        "phone": "string",
        "instagram": "string",
        "facebook": "string",
        "cpf": f"112341541",
    }
    cli = Client_Pydantic(**payload)
    res = await to_decorated(cli)
    assert res == cli.dict()


@pytest.mark.asyncio
async def test_patch_raises_HTTPException(client):
    @patch_items(model=ClientModel, pydantic=Client_Pydantic)
    async def to_decorated(item: Client_Pydantic):
        ...

    cli = Client_Pydantic(
        **{
            "id": 90000000,
            "first_name": "string",
            "last_name": "string",
            "email": "string",
            "phone": "string",
            "instagram": "string",
            "facebook": "string",
            "cpf": "string",
        }
    )

    with pytest.raises(HTTPException):
        await to_decorated(cli)
