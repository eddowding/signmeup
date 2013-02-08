import time

from django.utils.hashcompat import sha_constructor
from django.conf import settings

from mongoengine.document import Document
from mongoengine import fields
from templated_email import send_templated_mail

from localinfo.models import LocalInfo

class SignUp(Document):
    
    COLLECT = (
        'local_food',
        'open_late',
    )
    
    # Basic info
    name = fields.StringField(required=True)
    email = fields.EmailField(required=True)
    postcode = fields.StringField(required=True, name="Postcode", default="")
    location = fields.GeoPointField()
    
    mapit_info = fields.DictField()
    
    # Checkboxes
    local_food = fields.BooleanField(verbose_name="Local Food")
    open_late = fields.BooleanField(verbose_name="Late opening")
    
    token = fields.StringField()
    confirmed = fields.BooleanField(default=False)
    
    def generate_token(self):
        return sha_constructor(''.join(map(str, [
                settings.SECRET_KEY,
                self.__dict__,
                time.time()]))
        ).hexdigest()
    
    
    
    def save(self, *args, **kwargs):
        # New model
        NEW = False
        if not self.pk:
            NEW = True
            self.token = self.generate_token()

            send_templated_mail(
                template_name='new_signup',
                from_email='hello@sustaination.co',
                recipient_list=[self.email],
                context={
                    'token': self.token,
                    'name': self.name,
                    'email': self.email,
                    'postcode': self.postcode,
                }
            )
        
        m = super(SignUp, self).save(*args, **kwargs)
        
        if NEW:
            # For now, just update the whole coultry.  More to follow.
            area, created = LocalInfo.objects.get_or_create(type='country', name='UK')
            for key in self._fields:
                if key in self.COLLECT and bool(getattr(self, key)):
                    count = area.info.get(key, 0) + 1
                    area.info[key] = count
            area.save()
        
        return m