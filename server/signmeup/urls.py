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
    # Examples:
    # url(r'^$', 'signmeup.views.home', name='home'),
    # url(r'^signmeup/', include('signmeup.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # API
    (r'^api/', include(v1_api.urls)),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'', TemplateView.as_view(template_name="base.html")),
)

