"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import string
import random
from datetime import datetime

from django.test import TestCase
from django.db import models

from redisforms import forms

class FakeModel(models.Model):
    name = models.CharField(blank=True, max_length=100)
    
class FakeForm(forms.RedisMongoForm):
    class Meta:
        model = FakeModel

class SimpleTest(TestCase):
    def test_init(self):
        """
        Import with no model should break
        """
        self.assertRaises(ValueError, forms.ModelForm)
    
    def test_settings(self):
        self.assertTrue(forms.key_divider)
        self.assertTrue(isinstance(forms.key_divider, str))
        self.assertTrue(forms.site_id)
        self.assertTrue(forms.key_prefix)
    
    def test_save(self):
        f = FakeForm()
        f.name = "Foo"
        f.save()
    
    def test_model_key_prefix(self):
        f = FakeForm()
        self.assertTrue(f.model_key_prefix().endswith('FakeModel'))
    
    # def test_throughput(self):
    #     def random_string():
    #         return ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    # 
    #     def insert(number_of_records=1000):
    #         # strings = [random_string() for i in range(number_of_records)]
    #     
    #         start_time = datetime.now()
    #         for i in range(number_of_records):
    #             f = FakeForm()
    #             f.name = "foo"
    #             f.save()
    #         offset = datetime.now() - start_time
    #         import math
    #         print number_of_records, offset.microseconds, number_of_records/math.log(offset.microseconds)
    # 
    #     records = [
    #         1,
    #         10,
    #         100,
    #         1000,
    #         10000,
    #         100000,
    #     ]
    #     for n in records:
    #         insert(n)
        









        