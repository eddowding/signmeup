from django.test import TestCase
from django.test.utils import override_settings

from tastypie.test import ResourceTestCase

from models import SignUp
from localinfo.models import LocalInfo

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
        
    
    def test_create_view(self):
        self.client.get('/')


class APITests(ResourceTestCase):
    
    @override_settings(DEBUG=True)
    def test_post(self):
        data = {
            'name' : 'sym',
            'email' : 'sym.roe@talusdesign.co.uk',
            'postcode' : 'SE22 8DJ',
            'local_food' : True
        }
        
        info_model, created = LocalInfo.objects.get_or_create(type='country', name='UK')
        self.assertEqual(info_model.info, {})
        self.assertEqual(SignUp.objects.count(), 0)
        req = self.api_client.post(
            '/api/v1/signup/', 
            format='json',
            data=data
        )
        self.assertHttpCreated(req)
        # Verify a new one has been added.
        self.assertEqual(SignUp.objects.count(), 1)
        print 
        print 
        print 
        info_model = LocalInfo.objects.get(type='country', name='UK')
        print info_model.info
        
        self.assertEqual(info_model.info, {u'local_food': 1})
        print 
        print 
        print 

