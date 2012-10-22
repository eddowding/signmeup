"""
Redis forms are like normal model forms, with `save()` method overwritten.

Rather than saving to the database, the validated form object is saved in to a
redis hash and an ID is returned.

An example redis key for a model called 'Signee' might be:

1::redisforms::Signee::100

Where:

* `::` is `settings.REDISFORMS_KEY_DIVIDER (default `::`)
* `1` is settings.SITE_ID
* `redisforms` is constant
* `Signee` is the model name
* `100` is the result of redis.incr(1::redisforms::signee::pk), using the same
  key generation as above

"""
import time

from django.utils.hashcompat import sha_constructor
from mongotools.forms import MongoForm
from django.conf import settings

import redis
r = redis.Redis()

# settings
key_divider = getattr(settings, 'REDISFORMS_KEY_DIVIDER', '::')
site_id = getattr(settings, 'SITE_ID', 1)

def make_key(*args):
    return key_divider.join(map(str, args))


key_prefix = make_key(site_id,'redisforms')

class RedisMongoForm(MongoForm):
    
    def model_key_prefix(self):
        # print "\n".join(dir(self.instance._get_collection()))
        name =  self.instance._get_collection().name
        return make_key(key_prefix, name)
    
    def generate_token(self):
        return sha_constructor(''.join(map(str, [
                settings.SECRET_KEY,
                self.__dict__,
                time.time()]))
        ).hexdigest()
    
    
    def model_token(self, key):
        token = None
        while not token:
            token = self.generate_token()
            token_key = make_key('tokens', token)
            worked = r.setnx(token_key, key)
            if not worked:
                token = None
        r.expire(token_key, 1209600) # 2 weeks
        return token

    def save(self, commit=True):
        """
        Never save the form to the database.

        If `committed` is `True`, call the normal save method, as this will return
        an instance as expected.
        
        If `committed` is `False`, save in to redis.
        
        NOTE: this DOES NOT return a model.  It returns the dict that was saved 
        to redis with `pk` and `hash_key` as keys.
        """
        
        if not self.is_valid():
            raise ValueError("Form not valid")
        super(RedisMongoForm, self).save(commit=False)
        
        # Main logic for the save method.
        redis_pk = r.incr(make_key(self.model_key_prefix(), 'pk'))
        
        # Build the dict that will be saved as a hash
        redis_hash = self.cleaned_data
        
        p = r.pipeline()
        hash_key = make_key(self.model_key_prefix(), redis_pk)
        p.hmset(hash_key, redis_hash)
        p.sadd(make_key(self.model_key_prefix(), 'ids'), redis_pk)
        p.execute()
        redis_hash['pk'] = redis_pk
        redis_hash['hash_key'] = hash_key
        redis_hash['model_token'] = self.model_token(hash_key)
        r.sadd('unclaimed_tokens', redis_hash['model_token'])
        return redis_hash











