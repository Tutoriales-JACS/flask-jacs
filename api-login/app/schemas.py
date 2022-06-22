from app import ma
from marshmallow import fields

class UserSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String()
    password = fields.String()

class TokenSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    usuario_id = fields.Integer()
    token = fields.String(unique=True)

