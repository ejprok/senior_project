from django.db import models
# from events.widgets import *
from django_google_maps.fields import AddressField, GeoLocationField

# Create your models here.
from django.db import models
from django.urls import reverse

class Event(models.Model):
    title  = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    
    date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    start_time = models.TimeField(auto_now=False, auto_now_add=False, blank=True)
    end_time = models.TimeField(auto_now=False, auto_now_add=False, blank=True)
    
    address = AddressField(max_length=100)
    geolocation = GeoLocationField(blank=True)


    def __str__(self):
        return self.title

