from django.test import TestCase
# from django.core import mail

from django.test.utils import override_settings

from tastypie.test import ResourceTestCase

from models import SignUp
import forms

class SimpleTest(TestCase):
    def setUp(self):
        self.u = SignUp(
            name="Sym",
            postcode="SE22 8DJ",
            email="sym.roe@talusdesign.co.uk",
            local_food = True,
            open_late = False,
            )
        
    
    def test_model_init(self):
        self.u.save()
        
        # print User.objects.all()
    
    def test_form(self):
        pass
        # print forms.SignupForm()

    def test_form_save(self):
        f1 = forms.SignupForm({'name' : 'sym', 'email' : 'a@b.com',})
        f2 = forms.SignupForm({'name' : 'sym', 'email' : 'a@b.com', 'postcode' : 'foo'})

        self.assertFalse(f1.is_valid())
        self.assertRaises(ValueError, f1.save)
        self.assertTrue(f2.save)

        
    def test_token(self):
        f = forms.SignupForm(instance=self.u)
        f.model_token(1)
        
    def test_form_save_true(self):
        f = forms.SignupForm({
            'name' : 'sym', 
            'email' : 'a@b.com', 
            'postcode' : 'SE22 8DJ'
            })
        f.save()
    
    def test_create_view(self):
        self.client.get('/')


class APITests(ResourceTestCase):
    
    @override_settings(DEBUG=True)
    def test_post(self):
        data = {
            'name' : 'sym',
            'email' : 'sym.roe@talusdesign.co.uk',
            'postcode' : 'SE22 8DJ'
        }
        
        self.assertEqual(SignUp.objects.count(), 0)
        req = self.api_client.post(
            '/api/v1/signup/', 
            format='json',
            data=data
        )
        self.assertHttpCreated(req)
        # Verify a new one has been added.
        self.assertEqual(SignUp.objects.count(), 1)
    


        
    