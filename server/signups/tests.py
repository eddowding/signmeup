"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core import mail

from models import SignUp
import forms

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
    
    def setUp(self):
        self.u = SignUp(
            name="Sym",
            postcode="SE22 8DJ",
            email="sym.roe@talusdesign.co.uk"
            )
        
    
    def test_model_init(self):
        self.u.save()
        
        # print User.objects.all()
    
    def test_form(self):
        pass
        # print forms.SignupForm()

    def test_form_save(self):

        from mongotools.forms import MongoForm
        f1 = forms.SignupForm({'name' : 'sym', 'email' : 'a@b.com',})
        f2 = forms.SignupForm({'name' : 'sym', 'email' : 'a@b.com', 'postcode' : 'foo'})

        self.assertFalse(f1.is_valid())
        self.assertRaises(ValueError, f1.save)
        self.assertTrue(f2.save)

        
    def test_token(self):
        f = forms.SignupForm(instance=self.u)
        f.model_token(1)
        
    def test_email_body(self):
        f = forms.SignupForm({
            'name' : 'sym', 
            'email' : 'a@b.com', 
            'postcode' : 'SE22 8DJ'
            })
        f.save()
        # print mail.outbox[0].body
    
    def test_create_view(self):
        self.client.get('/')






        