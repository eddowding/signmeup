from mongoengine.document import Document
from mongoengine import fields

class LocalInfo(Document):
    # Basic info
    type = fields.StringField(required=True)
    name = fields.StringField(required=True)
    info = fields.DictField()
