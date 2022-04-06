from eyeapp.models import Application, Event
from rest_framework import serializers

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Application
        fields=('name','token')

class EventSerializer(serializers.ModelSerializer):
    related_application = serializers.PrimaryKeyRelatedField(queryset=Application.objects.all())
    class Meta:
        model=Event
        fields=('session_id','category','name','data','timestamp','related_application')
        #virgül koymayı sakın unutmayın,anlamadığım bir şekilde DRF ,bu alanının mutlaka bir liste ya da küme tipinde olmasını istiyor. Fields alanına eğer tek bir attribute ekleyeceksiniz mutlaka buna dikkat edin