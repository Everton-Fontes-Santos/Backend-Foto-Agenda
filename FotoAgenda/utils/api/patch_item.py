from functools import wraps

from fastapi.exceptions import HTTPException
from tortoise.contrib.pydantic.base import PydanticModel
from tortoise.exceptions import DoesNotExist
from tortoise.models import Model

from .not_found_entity import entity_not_found


def patch_items(model: Model, pydantic: PydanticModel):
    """
    Decorator returns one the item from model

    and return a pydantic schema.

    Args:
        model (Model): The Tortoise Model thats will be used
        pydantic (PydanticModel): the pydantic model schema to be returned to wrapper function

    """

    def wrapper(func):
        @entity_not_found
        @wraps(func)
        async def inner_wrapper(payload: PydanticModel):
            item = await model.filter(id=payload.id).first()
            if item:
                await item.update_from_dict(payload.dict())
                return await pydantic.from_tortoise_orm(item)

            raise DoesNotExist

        return inner_wrapper

    return wrapper
