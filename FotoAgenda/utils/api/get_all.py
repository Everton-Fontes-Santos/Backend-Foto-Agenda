from functools import wraps

from tortoise.contrib.pydantic.base import PydanticModel
from tortoise.exceptions import FieldError
from tortoise.models import Model

from .not_found_entity import entity_not_found


def get_all_itens(model: Model, pydantic: PydanticModel):
    """
    Decorator returns all the items from model

    and return a list of  pydantic schema.

    Args:
        model (Model): The Tortoise Model thats will be used
        pydantic (PydanticModel): the pydantic model schema to be returned to wrapper function
    """

    def wrapper(func):
        @entity_not_found
        @wraps(func)
        async def inner_wrapper():
            return await pydantic.from_queryset(model.all())

        return inner_wrapper

    return wrapper
