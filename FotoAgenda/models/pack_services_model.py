from tortoise import fields
from tortoise.models import Model


class clientModel(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=254)
    description = fields.TextField()
    price = fields.IntField()
    promotional_price = fields.IntField()
