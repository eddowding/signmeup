from mongoengine.document import Document
from mongoengine import fields

from mongoengine import connect
connect('signups')

class SignUp(Document):
    # Basic info
    name = fields.StringField(required=True)
    email = fields.EmailField(required=True)
    postcode = fields.StringField(required=True)
    
    # Checkboxes
    local_food = fields.BooleanField()
    open_late = fields.BooleanField()


class User(Document):
    name = fields.StringField()
    foo = fields.StringField()
    bar = fields.StringField()
    baz = fields.StringField()
    