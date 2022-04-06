from django.db import models
from jsonfield import JSONField
import uuid

class Application(models.Model):
    app_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    unique_name=models.CharField(max_length=30)
    token=models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=True)
    # sessions=models.ManyToManyField(Event)

def __str__(self):
        return self.name

class Event(models.Model):
    session_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category =  models.CharField(max_length=70)
    name = models.CharField(max_length=70)
    data= JSONField()
    timestamp = models.DateTimeField(auto_now=True)
    related_application = models.ForeignKey(Application,on_delete=models.CASCADE, related_name="application")
    
def __str__(self):
        return self.session_id

