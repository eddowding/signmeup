from django.views.generic import RedirectView
from django.http import Http404

from .models import SignUp

class ConfirmView(RedirectView):
    def get_redirect_url(self, **kwargs):
        try:
            signup = SignUp.objects.get(token=self.request.GET.get('token'))
        except:
            raise Http404
        signup.confirmed = True
        signup.save()
        return "/share/"
