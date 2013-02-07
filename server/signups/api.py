from tastypie_mongoengine import resources
from tastypie.authorization import Authorization
from models import SignUp

class SignUpResource(resources.MongoEngineResource):
    class Meta:
        queryset = SignUp.objects.all()
        allowed_methods = ('get','post')
        authorization = Authorization()
        filtering = {
            'location': resources.QUERY_TERMS_ALL
        }
    
    def dehydrate_email(self, bundle):
           return None
    
    def dehydrate_name(self, bundle):
           return None
    
    def build_filters(self, filters=None):
        if filters is None:
            filters = {}
        
        orm_filters = super(SignUpResource, self).build_filters(filters)
        
        if "within_distance" in filters:
            points = filters['within_distance'].split(',')
            points = map(float, points)
            distance = [
                (points[0],points[1]),
                5
            ]
            
            orm_filters["location__within_distance"] = distance
        
        return orm_filters
           