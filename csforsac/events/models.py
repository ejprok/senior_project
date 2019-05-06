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



from wagtailgmaps.edit_handlers import MapFieldPanel


from django.urls import reverse

class EventListingPage(Page):
    body = models.CharField(max_length=255, blank=True)
    event_listing_banner = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete= models.SET_NULL, 
    )
    content_panels = Page.content_panels + [
        FieldPanel('body'),
        ImageChooserPanel("event_listing_banner"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        all_entries = EventFocusPage.objects.all()

        context['events'] = all_entries
        return context
       
class EventFocusPage(Page):
	brief_description = RichTextField(blank=True)
	detailed_description = RichTextField(blank=True)
	address = models.CharField(max_length=255, blank=True)
	geolocation = models.CharField(max_length=255, blank=True)
	
	start_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
	end_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
	start_time = models.TimeField(auto_now=False, auto_now_add=False, blank=True)
	end_time = models.TimeField(auto_now=False, auto_now_add=False, blank=True)
	
	
	content_panels = Page.content_panels + [
		FieldPanel('brief_description'),
		FieldPanel('detailed_description'),
		MapFieldPanel('address'),
		MapFieldPanel('geolocation', latlng=True),
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



    def __str__(self):
        return self.title

