from events.models import Event, EventFocusPage
from rest_framework import serializers


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'description', 'date', 'start_time', 'end_time')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventFocusPage
        fields = ( 'title', 'description', 'start_date', 'end_date', 'start_time', 'end_time', 'slug')



