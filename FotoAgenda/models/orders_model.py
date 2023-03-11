from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model


class OrderModel(Model):
    id = fields.IntField(pk=True)
    client = fields.ForeignKeyField("models.ClientModel", related_name="client")
    observations = fields.TextField()


Order_Pydantic = pydantic_model_creator(OrderModel, name="Order")
