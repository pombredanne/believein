from django.db import models

class Hashtag(models.Model):
    # tweet max 140 - # = 139
    tag = models.CharField(max_length=139, primary_key=True)
    count = models.IntegerField(default=0)

    def increment(self):
        self.count = self.count + 1
        self.save()

    def json(self):
        return {
            "hashtag" : self.tag,
            "count" : self.count
        }