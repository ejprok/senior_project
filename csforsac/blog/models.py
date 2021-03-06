""" Blog Listing and Pages """
from django.db import models
from django.template.response import TemplateResponse
from django import forms
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# from wagtail.core import blocks # inherit this from blog_blocks
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.embeds.blocks import EmbedBlock
from streams import custom_blocks as blocks # custom blocks
from wagtail.core.blocks import RichTextBlock
from modelcluster.fields import ParentalKey


class BlogListingPage(Page):
    template = "blog/blog_listing_page.html"
    max_count = 1
    subpage_types = ['BlogFocusPage']

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
            all_posts = BlogFocusPage.objects.live().public().order_by('-first_published_at')
            
            paginator = Paginator(all_posts, 5)
            page = request.GET.get("page")
            try:
                posts = paginator.page(page)
            except PageNotAnInteger:
                posts = paginator.page(1)
            except EmptyPage:
                posts = paginator.page(paginator.num_pages)

            context["posts"] = posts
            return context


class BlogFocusPage(RoutablePageMixin, Page):
    template = "blog/blog_focus_page.html"
    subpage_types = []
    parent_page_types = ['blog.BlogListingPage']
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
        help_text = 'This image is scalled to 500 pixels tall',
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
            ("title_and_Subtitle", blocks.TitleAndSubtitle() ),
            ("full_richtext", blocks.RichtextBlock()),
            ("limited_richtext", blocks.LimitedRichtextBlock()),
            ("embedding", blocks.EmbeddedBlock()),
            ("card_block", blocks.CardBlock()),
            # ("cta", blocks.CTABlock()),
        ],
        null=True,
        blank=True,
    )
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("custom_title"),
            ImageChooserPanel("article_image"),

        ],
            heading ="titles and header",            
        ),
        MultiFieldPanel([
            FieldPanel("blog_summary"),
        ],
            heading ="Summary",
        ),

        MultiFieldPanel([
            StreamFieldPanel("content"),
        ],heading ="Body"),

    ]
    class meta: #noqa
        verbose_name = "Blog Post"
    