from django.shortcuts import render
from events.models import Event, EventFocusPage

from rest_framework import viewsets
from events.serializers import EventSerializer

# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
	queryset = EventFocusPage.objects.all()
	serializer_class = EventSerializer