from tastypie_mongoengine import resources
from tastypie.authorization import Authorization
from models import LocalInfo

class LocalInfoResource(resources.MongoEngineResource):
    class Meta:
        queryset = LocalInfo.objects.all()
        allowed_methods = ('get',)
        authorization = Authorization()
    