from django.conf.urls.defaults import url, patterns
from views import ConfirmView

urlpatterns = patterns('',
    url(r'^confirm/', ConfirmView.as_view(), name='confirm_view'),
)