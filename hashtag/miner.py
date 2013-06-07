from celery import task
from twython import TwythonStreamer
from models import Hashtag
from config import *

connected = False

class InStreamer(TwythonStreamer):
    connected = True
    
    def on_success(self, data):
        if not 'entities' in data:
            return
        if not 'hashtags' in data['entities']:
            return
        for tag_meta in data['entities']['hashtags']:
            tag = tag_meta['text']
            hashtag, created = Hashtag.objects.get_or_create(tag=tag)
            hashtag.increment()
        # done

    def on_limit(self, data):
        connected = False

    def on_disconnect(self, data):
        connected = False

@task()
def mine():    
    if connected:
        return
    stream = InStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    stream.statuses.filter(track = 'charity')
    return