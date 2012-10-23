import redis
r = redis.Redis()

from django.core.urlresolvers import reverse
from django.shortcuts import Http404
from django.utils.functional import lazy

from django.views.generic import TemplateView, RedirectView, FormView
from mongotools.views import CreateView
from djpjax import PJAXResponseMixin

from forms import SignupForm, PostcodeForm
from models import SignUp

class HomeView(FormView):
    form_class = PostcodeForm
    
    template_name = "home.html"
    
    def get_success_url(self):
        # import pdb
        # pdb.set_trace()
        postcode = self.request.POST['postcode'].replace(' ', '')
        url = reverse('postcode_details', kwargs={'postcode' : postcode})
        return url

class PostcodeDetails(PJAXResponseMixin, CreateView):
    form_class = SignupForm
    
    template_name = "postcode_details.html"
    pjax_template_name = "postcode_details_ahah.html"

    def get_initial(self):
        return {
            'postcode' : self.kwargs['postcode']
        }
        
    def get_success_url(self):
        return reverse('thanks')

        
class ThanksView(TemplateView):
    template_name = "thanks.html"

class ShareView(TemplateView):
    template_name = "share.html"


class ConfirmView(RedirectView):
    # template_name = "confirm.html"
    
    def get_redirect_url(self, **kwargs):
        return reverse('share')
    
    def clean_redis_dict(self, d):
        """
        The Redis client doesn't keep boolean types (True becomes 'True').
        
        Parse them out, and convert them back to booleans.
        """
        for k,v in d.items():
            if v in ("True", '1'):
                d[k] = True
            if v in ('False', '0'):
                d[k] = False
        return d
            
    def get(self, request, *args, **kwargs):
        token = kwargs['token']
        model_pk = r.get('tokens::%s' % token)
        if not model_pk:
            raise Http404
        model_dict = r.hgetall(model_pk)
        s = SignUp(**self.clean_redis_dict(model_dict))
        s.save()
        
        # Save worked, delete info from redis, preserving the key for now.
        
        # r.delete(model_pk)
        # r.srem('unclaimed_tokens', token)
        
        return super(ConfirmView, self).get(request, *args, **kwargs)
