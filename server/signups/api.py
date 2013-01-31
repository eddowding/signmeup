from tastypie_mongoengine import resources
# from tastypie.resources import ALL, ALL_WITH_RELATIONS
from models import SignUp

class SignUpResource(resources.MongoEngineResource):
    class Meta:
        queryset = SignUp.objects.all()
        allowed_methods = ('get',)
        filtering = {
            'location': resources.QUERY_TERMS_ALL
        }

    def build_filters(self, filters=None):
        if filters is None:
            filters = {}

        orm_filters = super(SignUpResource, self).build_filters(filters)

        if "within_box" in filters:
            points = filters['within_box'].split(',')
            points = map(float, points)
            box = [
                (points[0],points[1]),
                (points[2],points[3])
            ]
            orm_filters["location__within_box"] = box

        return orm_filters
           