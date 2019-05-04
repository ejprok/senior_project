from django.db import models
from django.template.response import TemplateResponse
from django import forms

# from wagtail.core import blocks
from streams import custom_blocks # custom blocks

from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.blocks import RichTextBlock


from django_google_maps.fields import AddressField, GeoLocationField


from django.urls import reverse

class EventListingPage(Page):
    body = models.CharField(max_length=255, blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    def get_context(self, request):
        all_entries = EventFocusPage.objects.all()

        context = { 'events' : all_entries}
        return context
       
class EventFocusPage(Page):
	description = models.CharField(max_length=255, blank=True)
	
	start_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
	end_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
	start_time = models.TimeField(auto_now=False, auto_now_add=False, blank=True)
	end_time = models.TimeField(auto_now=False, auto_now_add=False, blank=True)
	
	content_panels = Page.content_panels + [
	    FieldPanel('description'),
	    FieldPanel('start_date'),
	    FieldPanel('end_date'),
	    FieldPanel('start_time'),
	    FieldPanel('end_time'),
	]
	



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

