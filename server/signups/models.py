import time

from django.utils.hashcompat import sha_constructor
from django.conf import settings

from mongoengine.document import Document
from mongoengine import fields
from templated_email import send_templated_mail

from localinfo.models import LocalInfo

class SignUp(Document):
    
    COLLECT = (  
      'independent_biz',
      'veg_box',
      'group_buying',
      'csa',
      'supermarkets',
      'food_bank',
      'home_delivery',
      'longer_opening',
      'reduced_waste',
      'less_packaging',
      'work_food',
      'local_food',
      'seasonal_food',
      'organic_food',
      'ethnic_food',
      'cheaper_food',
      'branded_food',
      'healthy_ready_meals'
    )
    
    # Basic info
    name = fields.StringField(required=False)
    email = fields.EmailField(required=True)
    postcode = fields.StringField(required=True, name="Postcode", default="")
    location = fields.GeoPointField()
    
    mapit_info = fields.DictField()
    
    # Checkboxes
    local_food = fields.BooleanField(verbose_name="Local Food", default=False)
    independent_biz = fields.BooleanField(verbose_name="Independent business", default=False)
    group_buying = fields.BooleanField(verbose_name="Group buying", default=False)
    supermarkets = fields.BooleanField(verbose_name="Supermarkets", default=False)
    food_bank = fields.BooleanField(verbose_name="Food bank", default=False)
    home_delivery = fields.BooleanField(verbose_name="Home delivery", default=False)
    csa = fields.BooleanField(verbose_name="CSA", default=False)
    veg_box = fields.BooleanField(verbose_name="Veg box", default=False)
    longer_opening = fields.BooleanField(verbose_name="Longer opening", default=False)
    reduced_waste = fields.BooleanField(verbose_name="Reduced waste", default=False)
    less_packaging = fields.BooleanField(verbose_name="Less packaging", default=False)
    work_food = fields.BooleanField(verbose_name="Better food at work", default=False)
    seasonal_food = fields.BooleanField(verbose_name="Seasonal food", default=False)
    organic_food = fields.BooleanField(verbose_name="Organic food", default=False)
    ethnic_food = fields.BooleanField(verbose_name="Ethnic food", default=False)
    cheaper_food = fields.BooleanField(verbose_name="Cheaper food", default=False)
    branded_food = fields.BooleanField(verbose_name="Branded food", default=False)
    healthy_ready_meals = fields.BooleanField(verbose_name="Healthy ready meals", default=False)
    
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
                from_email=settings.DEFAULT_FROM_EMAIL,
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
                if key in self.COLLECT:
                    if bool(getattr(self, key)):
                        count = area.info.get(key, 0) + 1
                        area.info[key] = count
                    else:
                        area.info[key] = area.info.get(key, 0)
            area.save()
        
        return m