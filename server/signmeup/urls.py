from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from tastypie.api import Api

from signups.api import SignUpResource
from localinfo.api import LocalInfoResource

v1_api = Api(api_name='v1')
v1_api.register(SignUpResource())
v1_api.register(LocalInfoResource())

# if settings.DEBUG:
urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)


urlpatterns += patterns('',
    # API
    (r'^api/', include(v1_api.urls)),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'', TemplateView.as_view(template_name="base.html")),
)

