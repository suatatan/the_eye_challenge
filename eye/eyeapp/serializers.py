from eyeapp.models import Application, Event
from rest_framework import serializers

class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Application
        fields=('name','token','sessions')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields=('session_id','category','name','data','timestamp')
        #virgül koymayı sakın unutmayın,anlamadığım bir şekilde DRF ,bu alanının mutlaka bir liste ya da küme tipinde olmasını istiyor. Fields alanına eğer tek bir attribute ekleyeceksiniz mutlaka buna dikkat edin