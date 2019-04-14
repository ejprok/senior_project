""" Blog Listing and Pages """
from django.db import models
from django.template.response import TemplateResponse
from django import forms

# from wagtail.core import blocks # inherit this from blog_blocks
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel # idk what this is, but it's work keeping in mind maybe
from wagtail.embeds.blocks import EmbedBlock
from blog import blog_blocks as blocks # custom blocks
from wagtail.core.blocks import RichTextBlock


class BlogListingPage(Page):
    tempalate = "blog/blog_listing_page.html"
    custom_title = models.CharField(
        max_length=100,
        blank = True,
        null=False,
        help_text = 'type in the title for the blog listing page',
    )
    blog_listing_banner = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete= models.SET_NULL, 
    )
    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        ImageChooserPanel("blog_listing_banner"),
    ]
    def get_context(self, request, *args, **kwargs):
            context = super().get_context(request, *args, **kwargs)
            context["blogs"] = BlogFocusPage.objects.live().public() 
            # print("Printing blogs")
            # for blog in context["blogs"]:
            #     print("HERE are the blogs: ",blog)       
            return context


class BlogFocusPage(RoutablePageMixin, Page):
    tempalate = "blog/blog_focus_page.html"
    custom_title = models.CharField(
        max_length=100,
        blank = True,
        null=False,
        help_text = 'Type in the title for the blog article title',
    )
    article_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
    )
    blog_summary = models.TextField(
        max_length=255, 
        blank=False,
        null=True,
        help_text = 'Type in the summary for this blog article',
    )
    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichtextBlock()),
            ("limited_richtext", blocks.LimitedRichtextBlock()),
            ("embeding", blocks.EmbededBlock()),
            # ("Image", blocks.CardBlock()),
            # ("cta", blocks.CTABlock()),
        ],
        null=True,
        blank=True,
    )
    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        FieldPanel("blog_summary"),
        ImageChooserPanel("article_image"),
        StreamFieldPanel("content"),
    ]
    class meta: #noqa
        verbose_name = "Blog Post"
    def blog_page(self, request, *args, **kwargs):
        response = TemplateResponse(
            request, 'blog/blog_focus.html'
        )
        return response

