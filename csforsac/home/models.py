from django.db import models
from django.template.response import TemplateResponse

from wagtail.core import blocks
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


<<<<<<< HEAD
class HomePage(Page):
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
=======
class HomePage(RoutablePageMixin, Page):
    body = models.TextField(max_length=255)
    test_field = models.CharField(max_length=30, blank=True)
    extra = RichTextField(blank=True)
    more = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('extra'),
        FieldPanel('test_field'),
        FieldPanel('more'),
    ]
    @route(r'^home/$')
    def home_page(self, request, *args, **kwargs):
        
        response = TemplateResponse(
            request, 'home/contact_page.html'
        )
        return response

class AboutPage(RoutablePageMixin, Page):
    body = models.CharField(max_length=255, blank=True)
    test_field = models.CharField(max_length=30, blank=True)
    extra = RichTextField(blank=True)
    more = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('extra'),
        FieldPanel('test_field'),
        FieldPanel('more'),
    ]
 
    @route(r'^about/$')
    def about_page(self, request, *args, **kwargs):
        print("ye")
        response = TemplateResponse(
            request, 'home/about_page.html'
        )
        return response



>>>>>>> 2c0ed111059f52667476270a53cdf979744af2a6
