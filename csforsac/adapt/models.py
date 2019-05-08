"""" creating models in Adapt """

from django.db import models

from streams import custom_blocks
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel, MultiFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page



class AdaptPage(RoutablePageMixin, Page):
    template = "adapt/adapt_page.html"


    header_content = StreamField(custom_blocks.StreamLists().header_list,
        null=True,
        blank=True,)

    body = StreamField(custom_blocks.StreamLists().body_list,
        null=True,
        blank=True,
    )
    content_panels = Page.content_panels + [
       
        MultiFieldPanel([
            StreamFieldPanel("header_content"),
        ],heading ="Header"),

        MultiFieldPanel([
            StreamFieldPanel("body"),
        ],heading ="Page Contents"),

    ]
    class meta: #noqa
        verbose_name = "Adaptable Page"