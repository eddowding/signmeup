from mongoengine.document import Document
from mongoengine import fields

from localinfo.models import LocalInfo

class SignUp(Document):
    
    COLLECT = (
        'local_food',
        'open_late',
    )
    
    # Basic info
    name = fields.StringField(required=True)
    email = fields.EmailField(required=True)
    postcode = fields.StringField(required=True, name="Postcode")
    location = fields.GeoPointField()
    
    mapit_info = fields.DictField()
    
    # Checkboxes
    local_food = fields.BooleanField(verbose_name="Local Food")
    open_late = fields.BooleanField(verbose_name="Late opening")
    
    
    def save(self, *args, **kwargs):
        super(SignUp, self).save(*args, **kwargs)
        
        # For now, just update the whole coultry.  More to follow.
        area, created = LocalInfo.objects.get_or_create(type='country', name='UK')
        for key in self._fields:
            if key in self.COLLECT and bool(getattr(self, key)):
                count = area.info.get(key, 0) + 1
                area.info[key] = count
        area.save()
        