from functools import wraps

from tortoise.contrib.pydantic.base import PydanticModel
from tortoise.models import Model

from .not_found_entity import DoesNotExist, entity_not_found


def delete_item(model: Model, pydantic: PydanticModel):
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
        async def inner_wrapper(id: int):
            item = await model.filter(id=id).first()
            if item:
                item.delete()
                return {"message": "Deleted"}
            raise DoesNotExist

        return inner_wrapper

    return wrapper
