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


class StreamFieldList():
    """ This class holds generic lists of stream fields """

    header_stream_fields = [
        ("free_carousel", custom_blocks.FreeCarouselBlock()),
        ("wide_banner", custom_blocks.BannerWideImageBlock()),
    ]
    
    body_stream_fields = [
            ("title_and_Subtitle", custom_blocks.TitleAndSubtitle() ),
            ("full_richtext", custom_blocks.RichtextBlock()),
            ("limited_richtext", custom_blocks.LimitedRichtextBlock()),
            ("embeding", custom_blocks.EmbededBlock()),
            ("cards", custom_blocks.CardBlock()),
            ("right_featurettes", custom_blocks.LrgRightMediaBlock()),
            ("left_featurettes", custom_blocks.LrgLeftMediaBlock()),
            ("right_media_block", custom_blocks.SmRightMediaBlock()),
            ("left_media_block", custom_blocks.SmLeftMediaBlock()),
            ("centered_title", custom_blocks.CenteredTitle()),
        ]

class HomePage(Page):
    tempalate = 'home/home_page.html'

    # add pages into subpage_types in order to allow them to be child pages under the home_page
    # subpage_types = ['AboutPage','ContactPage','LearnPage','CollaboratePage','SupportPage','Implementation','adapt.AdaptPage']

    max_count = 1
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


class AboutPage(Page):
    tempalate = 'home/about_page.html'
    max_count = 1
    # Add pages to this parent_page_types list in order for this "about_page" to be a child page of additional pages.
    parent_page_types = ['home.HomePage']

    main_title = models.TextField(max_length=255, blank=True)
    quote1 = models.TextField(max_length=255, blank=True)
    quote2 = models.TextField(max_length=400, blank=True)
    quote3 = models.TextField(max_length=400, blank=True)
    col_1_header = models.TextField(max_length=375, blank=True)
    col_2_header = models.TextField(max_length=375, blank=True)
    col_3_header = models.TextField(max_length=375, blank=True)
    col_1_body = models.TextField(max_length=375, blank=True)
    col_2_body = models.TextField(max_length=375, blank=True)
    col_3_body = models.TextField(max_length=375, blank=True)
    goal_intro = models.TextField(max_length=375, blank=True)
    goal1 = models.TextField(max_length=200, blank=True)
    goal2 = models.TextField(max_length=200, blank=True)
    goal3 = models.TextField(max_length=200, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('main_title'),
            FieldPanel('quote1'),
            FieldPanel('quote2'),
            FieldPanel('col_1_header'),
            FieldPanel('col_1_body'),
            FieldPanel('col_2_header'),
            FieldPanel('col_2_body'),
            FieldPanel('col_3_header'),
            FieldPanel('col_3_body'),
            FieldPanel('quote3'),
            FieldPanel('goal_intro'),
            FieldPanel('goal1'),
            FieldPanel('goal2'),
            FieldPanel('goal3'),
        ],
        heading ="Body",        
        ),
    ]

class ContactPage(Page):
    tempalate = 'home/contact_page.html'
    max_count = 1
    header  = models.TextField(max_length=255, blank=True)
    subheader = models.TextField(max_length=255, blank=True)
    email_title = models.TextField(max_length=255, blank=True)
    email_sub_info = models.TextField(max_length=255, blank=True)
    phone_title = models.TextField(max_length=255, blank=True)
    phone_sub_info = models.TextField(max_length=255, blank=True)
    address_title = models.TextField(max_length=255, blank=True)
    address_sub_info = models.TextField(max_length=255, blank=True)
    content_panels = Page.content_panels + [
         MultiFieldPanel([
            FieldPanel('header'),
            FieldPanel('subheader'),
            FieldPanel('email_title'),
            FieldPanel('email_sub_info'),
            FieldPanel('phone_title'),
            FieldPanel('phone_sub_info'),
            FieldPanel('address_title'),
            FieldPanel('address_sub_info'),
        ],
        heading ="Body",        
        ),
    ]


class LearnPage(Page):
    max_count = 1
    template = 'home/learn_page.html'
    header_content = header_content = StreamField(StreamFieldList.header_stream_fields,null=True,blank=True)

    body = StreamField(StreamFieldList.body_stream_fields, null=True, blank=False)
    content_panels = Page.content_panels + [
       
        MultiFieldPanel([
            StreamFieldPanel("header_content"),
        ],heading ="Header"),

        MultiFieldPanel([
            StreamFieldPanel("body"),
        ],heading ="Page Contents"),

    ]
 


class CollaboratePage(Page):
    template = 'home/collaborate_page.html'
    max_count = 1
    header_content = StreamField(StreamFieldList.header_stream_fields,null=True, blank=True)

    elementary = StreamField(StreamFieldList.body_stream_fields, null=True, blank=False)
    middle_school = StreamField(StreamFieldList.body_stream_fields, null=True, blank=False)
    high_school = StreamField(StreamFieldList.body_stream_fields, null=True, blank=False)

    content_panels = Page.content_panels + [
       
        MultiFieldPanel([
            StreamFieldPanel("header_content"),
        ], 
        heading ="Header (optional)",        
        classname="collapsible collapsed"),

        MultiFieldPanel([
            StreamFieldPanel("elementary"),
        ], heading ="elementary",
        classname="collapsible collapsed"
        ),

        MultiFieldPanel([
            StreamFieldPanel("middle_school"),
        ], heading ="Middle School",
        classname="collapsible collapsed"
        ),

        MultiFieldPanel([
            StreamFieldPanel("high_school"),
        ], heading ="High School",
        classname="collapsible collapsed"
        ),
    ]
 


class SupportPage(Page):
    template = 'home/support_page.html'
    max_count = 1
    header_content = StreamField(StreamFieldList.header_stream_fields,null=True,blank=True)

    body = StreamField(StreamFieldList.body_stream_fields, null=True, blank=False)
    content_panels = Page.content_panels + [
       
        MultiFieldPanel([
            StreamFieldPanel("header_content"),
        ],heading ="Header"),

        MultiFieldPanel([
            StreamFieldPanel("body"),
        ],heading ="Page Contents"),

    ]

class ImplementationPage(Page):
    max_count = 1
    template = 'home/implementation_page.html'

    header_content = header_content = StreamField(StreamFieldList.header_stream_fields,null=True,blank=True)

    body = StreamField(StreamFieldList.body_stream_fields, null=True, blank=False)
    content_panels = Page.content_panels + [
        
        MultiFieldPanel([
            StreamFieldPanel("header_content"),
        ],heading ="Header"),

        MultiFieldPanel([
            StreamFieldPanel("body"),
        ],heading ="Page Contents"),

    ]
        

class StreamFieldList():
    """ This class holds generic lists of stream fields """

    header_stream_fields = [
        ("free_carousel", custom_blocks.FreeCarouselBlock()),
        ("wide_banner", custom_blocks.BannerWideImageBlock()),
    ]

    body_stream_fields = [
            ("title_and_Subtitle", custom_blocks.TitleAndSubtitle() ),
            ("full_richtext", custom_blocks.RichtextBlock()),
            ("limited_richtext", custom_blocks.LimitedRichtextBlock()),
            ("embeding", custom_blocks.EmbededBlock()),
            ("cards", custom_blocks.CardBlock()),
            ("right_featurettes", custom_blocks.LrgRightMediaBlock()),
            ("left_featurettes", custom_blocks.LrgLeftMediaBlock()),
            ("right_media_block", custom_blocks.SmRightMediaBlock()),
            ("left_media_block", custom_blocks.SmLeftMediaBlock()),
            ("centered_title", custom_blocks.CenteredTitle()),
        ]

"""
Orderable class example 
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
