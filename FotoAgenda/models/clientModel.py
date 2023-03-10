from tortoise import fields
from tortoise.models import Model


class clientModel(Model):
    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=254)
    last_name = fields.CharField(max_length=254)
    email = fields.CharField(max_length=254)
    phone = fields.CharField(max_length=20)
    instagram = fields.CharField(max_length=254)
    facebook = fields.CharField(max_length=254)
    cpf = fields.CharField(max_length=11, unique=True)
