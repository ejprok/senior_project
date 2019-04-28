
# Create your models here.
"""
This file is unneeded unless you need it for some reason

for now - notes
"""

# from django.db import models
# from django.db import models

# from streams import custom_blocks
# from wagtail.contrib.routable_page.models import RoutablePageMixin, route
# from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel, MultiFieldPanel
# from wagtailimages import ImageChooserPanel
# from wagtail.core.fields import RichTextField, StreamField
# from wagtail.core.models import Orderable


# class BasicCarouselImages(Orderable):
# """ 
# Use this orderable in your page for more control of the Carousel Image!
# Extend this orderable model into your model.py and overide this: 
# page = ParentalKey("your_app.YourPageOfInterest", related_name = "your_reference_name") 
# Insert this into your page's content_panels:
# InlinePanel("your_reference_name")

# """
    
    # reference related_name in HomePage
    # page = ParentalKey("", related_name = "basic_carousel") 
    # basic_carousel = models.ForeignKey(
    #     "wagtailimages.Image",
    #     null =True,
    #     blank=False,
    #     on_delete=models.SET_NULL,
    #     related_name="+"
    # )
    # panels = [
    #     ImageChooserPanel("basic_carousel")
    # ]

