from functools import wraps

from tortoise.contrib.pydantic.base import PydanticModel
from tortoise.models import Model

from .not_found_entity import entity_not_found


def get_by_id(model: Model, pydantic: PydanticModel):
    """
    Decorator returns all the items from model

    and return a list of  pydantic schema.

    Args:
        model (Model): The Tortoise Model thats will be used
        pydantic (PydanticModel): the pydantic model schema to be returned to wrapper function
        relateds (list[str]): A list of all relations of model to prefecth

    """

    def wrapper(func):
        @entity_not_found
        @wraps(func)
        async def inner_wrapper(id: int):
            items = await pydantic.from_queryset(model.filter(id=id))
            return items

        return inner_wrapper

    return wrapper
