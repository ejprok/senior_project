from django.db import models
from django.template.response import TemplateResponse

from wagtail.core import blocks
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

import feedparser # To get a feel from medium.com


""" 
Plan:
Insert URL of articles:
    use beautiful soup.
        # this holds whole article
        grab class = " section-inner sectionLayout--insetColumn " OR  <div class="section-content">
            This contains whole article with various sections:
            Headers
            Images
    Store this data in database
    
Grab new URLS from feed (follow url to get the article with the method described above)
            


object feed
    feed
    entries # appears to have all the articles
    bozo
    headers
    href
    status
    encoding
    version
    namespaces

Anatomy of a feed.entries
    can be 'content'(whole article) or 'summary_detail' (just a summary)

"""
class BlogListingPage(Page):

    def get_featured_authors():
        list_of_authors = [
            '@samuel.fare',
            '@amalong',
            '@ratracegrad'
        ]
        return list_of_authors

    def get_featured_authors():
       
        list_featured_articles= [
            'https://medium.com/@amalong/hacking-education-d4047e5d5a29',       
            'https://medium.com/techspiration-ideas-making-it-happen/when-the-heck-did-learning-to-code-become-cool-2e953f1c5efb'
        ]
        return list_featured_articles



    def get_context(self, request):
            feed = feedparser.parse('https://medium.com/feed/@amalong')
            # feed = feedparser.parse('https://medium.com/feed/@samuel.fare')
            articles = []
            for elem in feed.entries:
                # only append if article is a full article
                if 'content' in elem: 
                    print('next element : ', elem.title)

                    for cont_elem in elem.content:
                        print("NEXT IN CONTENT: ", cont_elem)

                    articles.append(elem)
                
            print (feed.feed.generator_detail)


            context ={
                'articles' : articles,
                
            }
            return context


  



class BlogFocusPage(RoutablePageMixin, Page):
    tempalate = "blog/blog_focus.html"

    # @TODO add steamfields
    # content = StreamFields()

    def blog_page(self, request, *args, **kwargs):
        response = TemplateResponse(
            request, 'blog/blog_focus.html'
        )
        return response