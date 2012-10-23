from django.conf.urls.defaults import patterns, url

from views import HomeView, ThanksView, ConfirmView, ShareView, PostcodeDetails

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='homeview'),
    url(r'^postcode/(?P<postcode>[^/]+)/$', PostcodeDetails.as_view(), name='postcode_details'),
    url(r'confirm/(?P<token>[^/]+)/$', ConfirmView.as_view(), name='confirm'),
    url(r'thanks/$', ThanksView.as_view(), name='thanks'),
    url(r'share/$', ShareView.as_view(), name='share'),
)