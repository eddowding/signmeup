from django.conf.urls.defaults import patterns, url

from views import HomeView, ThanksView, ConfirmView, ShareView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='homeview'),
    url(r'confirm/(?P<token>[^/]+)/$', ConfirmView.as_view(), name='confirm'),
    url(r'thanks/$', ThanksView.as_view(), name='thanks'),
    url(r'share/$', ShareView.as_view(), name='share'),
)