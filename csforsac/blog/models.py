from django.db import models
from django.template.response import TemplateResponse

from wagtail.core import blocks
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

import feedparser # To get a feel from medium.com


""" 
Anatomy of a feed:
    title
    title_detail
    subtitle
    subtitle_detail
    links
    link
    image
    generator_detail
    generator
    updated
    updated_parsed
    publisher
    publisher_detail


"""
class BlogListingPage(Page):
    """ This is going to list all the blog pages that we have """
    """ Do we make all the blogs"""
    print( "In blog_page method")

    # body = models.CharField(max_length=255, blank=True)
    # content_panels = Page.content_panels + [
    #         FieldPanel('body'),
    # ]

    def get_context(self, request):
            # feed = feedparser.parse('https://medium.com/feed/@amalong')
            feed = feedparser.parse('https://medium.com/feed/@samuel.fare')
          
            for elem in feed.feed:
                print('next element : ',elem)
                
            context ={
                'title' : feed.feed.title,
                'sub-Title' : feed.feed.subtitle,
                'image' : feed.feed.image,
                'publisher' : feed.feed.publisher,
                
            }
            return context

    # custom_title = models.CharField(
    #     max_length=100,
    #     blank=False,
    #     null=False,
    #     help_text='overwrite the default title',
    # )

    # def get_context(self, request, *args,**kwargs):
    #     """ Adding blogs to our context """
    #     context = super().get_context(request, *args. **kwargs)
    #     return context
    # def get_context(self, request, *args, **kwargs):
    #     print( "In blog_page method")

    #     entire_feed = feedparser.parse('https://medium.com/feed/@amalong')
    #     # print("whole feed ",entire_feed)
    #     body = models.CharField(max_length=255, blank=True)
    #     content_panels = Page.content_panels + [
    #             FieldPanel('body'),
    #     ]

  



class BlogFocusPage(RoutablePageMixin, Page):
    tempalate = "blog/blog_focus.html"

    # @TODO add steamfields
    # content = StreamFields()

    def blog_page(self, request, *args, **kwargs):
        response = TemplateResponse(
            request, 'blog/blog_focus.html'
        )
        return response