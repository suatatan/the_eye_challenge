from django.db import models
from jsonfield import JSONField
import uuid

class Event(models.Model):
    session_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category =  models.CharField(max_length=70)
    name = models.CharField(max_length=70)
    data= JSONField()
    timestamp = models.DateTimeField(auto_now=True)
    
def __str__(self):
        return self.session_id

class Application(models.Model):
    name=models.CharField(max_length=30)
    token=models.CharField(max_length=30)
    sessions=models.ManyToManyField(Event)
