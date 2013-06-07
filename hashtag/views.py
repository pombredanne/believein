import json
from django.http import HttpResponse
from models import Hashtag
from miner import mine

def home(request):
    mine.delay()
    data = [tag.json() for tag in Hashtag.objects.all()]
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type="application/json"
    )