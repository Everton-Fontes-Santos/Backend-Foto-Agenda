from functools import wraps

from fastapi import HTTPException
from tortoise.contrib.pydantic.base import PydanticModel
from tortoise.exceptions import DoesNotExist
from tortoise.models import Model


def entity_not_found(func):
    """
    Decorator returns all the items from model

    and return a list of  pydantic schema.

    Args:
        model (Model): The Tortoise Model thats will be used
        pydantic (PydanticModel): the pydantic model schema to be returned to wrapper function
        relateds (list[str]): A list of all relations of model to prefecth

    """

    @wraps(func)
    async def inner_wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)

        except DoesNotExist:
            raise HTTPException(status_code=404, detail="Entity not found")

    return inner_wrapper
