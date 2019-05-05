"""" creating models in Adapt """

from django.db import models

from streams import custom_blocks
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel, MultiFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page



class AdaptPage(RoutablePageMixin, Page):
    tempalate = "adapt/adapt_page.html"


    header_content = StreamField(
        [
            ("free_carousel", custom_blocks.FreeCarouselBlock()),
        ],
        null=True,
        blank=True,
    )

    body = StreamField(
        [
            ("title_and_Subtitle", custom_blocks.TitleAndSubtitle() ),
            ("full_richtext", custom_blocks.RichtextBlock()),
            ("limited_richtext", custom_blocks.LimitedRichtextBlock()),
            ("embeding", custom_blocks.EmbededBlock()),
            ("cards", custom_blocks.CardBlock()),
            # ("card_row", custom_blocks.CardRow()),
            ("right_featurettes", custom_blocks.LrgRightMediaBlock()),
            ("left_featurettes", custom_blocks.LrgLeftMediaBlock()),
            ("right_media_block", custom_blocks.SmRightMediaBlock()),
            ("left_media_block", custom_blocks.SmLeftMediaBlock()),
            
        ],
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