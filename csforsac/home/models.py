from django.db import models
from django.template.response import TemplateResponse
from django import forms

# from wagtail.core import blocks
from streams import custom_blocks # custom blocks

from wagtail.contrib.routable_page.models import route #, RoutablePageMixin
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.blocks import RichTextBlock

from events.models import Event

class HomePage(Page):
    tempalate = 'home/home_page.html'
    carousel_1_header = models.TextField(max_length=255, blank=True)
    carousel_1_body = models.TextField(max_length=255, blank=True)
    carousel_2_header = models.TextField(max_length=255, blank=True)
    carousel_2_body = models.TextField(max_length=255, blank=True)
    carousel_3_header = models.TextField(max_length=255, blank=True)
    carousel_3_body = models.TextField(max_length=255, blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('carousel_1_header'),
        FieldPanel('carousel_1_body'),
        FieldPanel('carousel_2_header'),
        FieldPanel('carousel_2_body'),
        FieldPanel('carousel_3_header'),
        FieldPanel('carousel_3_body'),
    ]
    # def home_page(self, request, *args, **kwargs):
    #     response = TemplateResponse(
    #         request, 'home/home_page.html'
    #     )
    #     return response


class AboutPage(Page):
    tempalate = 'home/about_page.html'

    body = models.CharField(max_length=255, blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
    # def about_page(self, request, *args, **kwargs):
    #     response = TemplateResponse(
    #         request, 'home/about_page.html'
    #     )
    #     return response

class ContactPage(Page):
    tempalate = 'home/contact_page.html'
    header  = models.TextField(max_length=255, blank=True)
    subheader = models.TextField(max_length=255, blank=True)
    email_title = models.TextField(max_length=255, blank=True)
    email_sub_info = models.TextField(max_length=255, blank=True)
    phone_title = models.TextField(max_length=255, blank=True)
    phone_sub_info = models.TextField(max_length=255, blank=True)
    address_title = models.TextField(max_length=255, blank=True)
    address_sub_info = models.TextField(max_length=255, blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('header'),
        FieldPanel('subheader'),
        FieldPanel('email_title'),
        FieldPanel('email_sub_info'),
        FieldPanel('phone_title'),
        FieldPanel('phone_sub_info'),
        FieldPanel('address_title'),
        FieldPanel('address_sub_info'),
    ]
    # def contact_page(self, request, *args, **kwargs):
    #     response = TemplateResponse(
    #         request, 'home/contact_page.html'
    #     )
    #     return response


class LearnPage(Page):
    template = 'home/learn_page.html'
    body = models.CharField(max_length=255, blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
 
    # def learn_page(self, request, *args, **kwargs):
    #     response = TemplateResponse(
    #         request, 'home/learn_page.html'
    #     )
    #     return response


class CollaboratePage(Page):
    template = 'home/collaborate_page.html'
    body = models.CharField(max_length=255, blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
 
    # def collab_page(self, request, *args, **kwargs):
    #     response = TemplateResponse(
    #         request, 'home/collaborate_page.html'
    #     )
    #     return response


class SupportPage(Page):
    template = 'home/collaborate_page.html'
    body = models.CharField(max_length=255, blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
 
    # def support_page(self, request, *args, **kwargs):
    #     response = TemplateResponse(
    #         request, 'home/support_page.html'
    #     )
    #     return response
        
        

# class EventsPage(Page):
#     body = models.CharField(max_length=255, blank=True)
#     content_panels = Page.content_panels + [
#         FieldPanel('body'),
#     ]

#     def get_context(self, request):
#         all_entries = Event.objects.all()

#         context = { 'events' : all_entries}
#         return context
        
        
# class MapPage(Page):
#     body = models.CharField(max_length=255, blank=True)
#     content_panels = Page.content_panels + [
#         FieldPanel('body'),
#     ]

#     def get_context(self, request):
#         all_entries = Event.objects.all()

#         context = { 'events' : all_entries}
#         return context


"""
Orderable classes 
"""
# class BasicCarouselImages(Orderable):
#       # reference related_name in HomePage
#     page = ParentalKey("home.HomePage", related_name = "basic_carousel") 
#     basic_carousel = models.ForeignKey(
#         "wagtailimages.Image",
#         null =True,
#         blank=False,
#         on_delete=models.SET_NULL,
#         related_name="+"
#     )
#     panels = [
#         ImageChooserPanel("basic_carousel")
#     ]

# Not even close to working yet
# class NavBar(Page):
#     tempalate = "nav_bar/nav_bar.html"

#     content = StreamField(
#         [
#             ("nav_title_link", CustomBlocks.NavLink()),
#             ("nav_drop_list", CustomBlocks.NavDropList()),
#         ],
#         null=True,
#         blank=True,
#     )
#     content_panels = Page.content_panels + [
#         StreamFieldPanel("content"),
#     ]
