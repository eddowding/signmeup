# -*- coding: utf-8 -*-
from django.conf import settings
from django import forms
from django.contrib.localflavor.uk.forms import UKPostcodeField
from django.contrib.sites.models import get_current_site

from templated_email import send_templated_mail
from redisforms.forms import RedisMongoForm
from mongotools.forms import MongoForm

from models import SignUp

class SignupForm(RedisMongoForm):
    class Meta:
        document = SignUp
    
    name = forms.CharField()
    postcode = UKPostcodeField()
    
    def save(self, commit=True):
        # Send an email when the form has been saved
        redis_form = super(SignupForm, self).save(commit=commit)
        
        send_templated_mail(
                template_name='confirm',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[redis_form['email']],
                context={
                    'form' : redis_form,
                    'site' : get_current_site(settings.SITE_ID),
                },
        )
