from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model


class PackServicesModel(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=254)
    description = fields.TextField()
    price = fields.IntField()
    promotional_price = fields.IntField()


PackService_Pydantic = pydantic_model_creator(PackServicesModel, name="PackService")
