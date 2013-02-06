from django.conf.urls.defaults import url
from tastypie_mongoengine import resources
from tastypie.authorization import Authorization
from models import LocalInfo

class LocalInfoResource(resources.MongoEngineResource):
    class Meta:
        queryset = LocalInfo.objects.all()
        allowed_methods = ('get',)
        authorization = Authorization()
        filtering = {
            'type' : resources.QUERY_TERMS_ALL,
            'name' : resources.QUERY_TERMS_ALL,
        }

    def override_urls(self):
            return [
                url(r"^(?P<resource_name>%s)/(?P<name>[\w\d_.-]+)/$" % 
                    self._meta.resource_name, 
                    self.wrap_view('dispatch_detail'), 
                    name="api_dispatch_detail"),
            ]