import sys
import csv
import urllib2
import json

from django.core.management.base import BaseCommand, CommandError
from signups.models import SignUp

def postcode_to_latlng(postcode):
    res = urllib2.urlopen('http://mapit.mysociety.org/postcode/%s' % postcode.replace(' ', '')).read()
    d = json.loads(res)
    return (d['wgs84_lat'], d['wgs84_lon'])

class Command(BaseCommand):
    def handle(self, *args, **options):
        # data = csv.DictReader(sys.stdin.readlines())
        # for line in data:
        #     s = SignUp()
        #     s.location = postcode_to_latlng(line['postcode'])
        #     s.name = line['name']
        #     s.postcode = line['postcode']
        #     s.email = "none@example.com"
        #     s.save()

        # from signups.models import SignUp
        # print SignUp.objects.filter(
        #     location__within_distance= 
        #         [
        #             (51.471493077591596, -0.02068519592285156),
        #             2
        #         ]
        #     )
        # print 
        # print SignUp.objects.filter(
        #     location__within_box= 
        #         [
        #             (51.44839066445258, -0.14428138732910156),
        #             (51.471493077591596, -0.02068519592285156)
        #         ]
        #     )
            