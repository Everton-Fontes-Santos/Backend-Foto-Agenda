from functools import wraps

from fastapi.exceptions import HTTPException
from tortoise.contrib.pydantic.base import PydanticModel
from tortoise.exceptions import IntegrityError
from tortoise.models import Model

from .not_found_entity import entity_not_found


def post_items(model: Model, pydantic: PydanticModel):
    """
    Decorator returns one the item from model

    and return a pydantic schema.

    Args:
        model (Model): The Tortoise Model thats will be used
        pydantic (PydanticModel): the pydantic model schema to be returned to wrapper function

    """

    def wrapper(func):
        @wraps(func)
        async def inner_wrapper(items: list[PydanticModel]):
            res = []
            try:
                for item in items:
                    item_obj = model(**item.dict())
                    await item_obj.save()
                    res.append(await pydantic.from_tortoise_orm(item_obj))
                return res
            except IntegrityError:
                raise HTTPException(status_code=500, detail="Already add")

        return inner_wrapper

    return wrapper
