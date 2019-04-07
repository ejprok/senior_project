from django.db import models
from django.template.response import TemplateResponse

from wagtail.core import blocks
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(RoutablePageMixin, Page):
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

    def home_page(self, request, *args, **kwargs):
        response = TemplateResponse(
            request, 'home/home_page.html'
        )
        return response

class AboutPage(RoutablePageMixin, Page):
    body = models.CharField(max_length=255, blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
 
    def about_page(self, request, *args, **kwargs):
        response = TemplateResponse(
            request, 'home/about_page.html'
        )
        return response



class ContactPage(RoutablePageMixin, Page):
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
 
    def contact_page(self, request, *args, **kwargs):
        response = TemplateResponse(
            request, 'home/contact_page.html'
        )
        return response


class LearnPage(RoutablePageMixin, Page):
    body = models.CharField(max_length=255, blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
 
    def learn_page(self, request, *args, **kwargs):
        response = TemplateResponse(
            request, 'home/learn_page.html'
        )
        return response


class CollaboratePage(RoutablePageMixin, Page):
    body = models.CharField(max_length=255, blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
 
    def collab_page(self, request, *args, **kwargs):
        response = TemplateResponse(
            request, 'home/collaborate_page.html'
        )
        return response


class SupportPage(RoutablePageMixin, Page):
    body = models.CharField(max_length=255, blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
 
    def support_page(self, request, *args, **kwargs):
        response = TemplateResponse(
            request, 'home/support_page.html'
        )
        return response

