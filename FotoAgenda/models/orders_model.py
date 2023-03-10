
from tortoise import fields
from tortoise.models import Model


class OrderModel(Model):
    id = fields.IntField(pk=True)
    client = fields.ForeignKeyField("models.ClientModel", related_name="client")
    observations = fields.TextField()
