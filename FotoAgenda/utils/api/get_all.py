from functools import wraps

from tortoise.contrib.pydantic.base import PydanticModel
from tortoise.models import Model
from utils.logger import logger

log = logger()


def get_all_itens(model: Model, pydantic: PydanticModel):
    def wrapper(func):
        wraps(func)

        async def inner_wrapper():
            try:
                items = await pydantic.from_queryset(model.all())
            except Exception:
                items = []
            return await func(items)

        return inner_wrapper

    return wrapper
