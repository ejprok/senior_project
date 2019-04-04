from django.db import models
from django.template.response import TemplateResponse

from wagtail.core import blocks
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

class BlogFocusPage(RoutablePageMixin, Page):
    tempalate = "blog/glob_focus.html"

    # @TODO add steamfields
    # content = StreamFields()

    @route(r'^/$')
    def blog_page(self, request, *args, **kwargs):
        response = TemplateResponse(
            request, 'blog/glob_focus.html'
        )
        return response

class BlogListingPage(RoutablePageMixin, Page):
    tempalate = "blog/glob_listing.html"

    # @TODO add steamfields
    # content = StreamFields()

    @route(r'^/$')
    def blog_page(self, request, *args, **kwargs):
        response = TemplateResponse(
            request, 'blog/glob_listing.html'
        )
        return response