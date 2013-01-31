# -*- coding: utf-8 -*-
from django.conf import settings
from django import forms
from django.contrib.localflavor.uk.forms import UKPostcodeField
from django.contrib.sites.models import get_current_site

from templated_email import send_templated_mail
from redisforms.forms import RedisMongoForm
from mongotools.forms import MongoForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, MultiField, ButtonHolder, Submit, Field, Row, Hidden

from django import forms
from django.forms.widgets import HiddenInput

from models import SignUp

class PostcodeForm(forms.Form):
    
    postcode = UKPostcodeField()

class SignupForm(RedisMongoForm):
    
    def __init__(self, *args, **kwargs):
        
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                'Step 1: tell us what you want',
                'local_food',
                'open_late'
            ),
            Fieldset(
                u'Step 2: we’ll collect and map this demand&hellip;',
                'email',
                
            )
        )
        self.helper.add_input(Submit('submit', 'Sign up'))
        super(SignupForm, self).__init__(*args, **kwargs)
        
        self.fields['postcode'].widget = HiddenInput()
        
    
    class Meta:
        document = SignUp
        exclude = ('location',)
    
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
