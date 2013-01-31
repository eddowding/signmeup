from mongoengine.document import Document
from mongoengine import fields


class SignUp(Document):
    # Basic info
    name = fields.StringField(required=True)
    email = fields.EmailField(required=True)
    postcode = fields.StringField(required=True, name="Postcodeasd")
    location = fields.GeoPointField()
    
    # Checkboxes
    local_food = fields.BooleanField(verbose_name="Local Food")
    open_late = fields.BooleanField(verbose_name="Late opening")
