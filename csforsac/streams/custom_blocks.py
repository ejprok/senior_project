"""" Custom blocks for streaming to apps """

from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock # can we figure out how to embed youtube
from wagtail.images.blocks import ImageChooserBlock

class TitleAndSubtitle(blocks.StructBlock):
    """ Typical Header """

    title = blocks.CharBlock(required=False, help_text="Add your title")
    sub_title = blocks.CharBlock(required=False, help_text="Add your sub-title")
    class Meta:  # noqa
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title and Subtitle"

class RichtextBlock(blocks.RichTextBlock):
    """ Richtext """

    class Meta:  # noqa
        template = "streams/basic_block.html"
        icon = "doc-full"
        label = "Full Richtext"


class LimitedRichtextBlock(blocks.RichTextBlock):
    """Richtext with only limited features."""

    def __init__(
        self, required=True, help_text=None, editor="default", features=None, **kwargs
    ):  # noqa
        super().__init__(**kwargs)
        self.features = ["bold", "italic", "link","ol", "ul"]

    class Meta:  # noqa
        template = "streams/basic_block.html" # 
        icon = "edit"
        label = "Limited Richtext"

class EmbededBlock(EmbedBlock):
    """ use rich text stream field instead """

    class Meta:  # noqa
        template = "streams/basic_block.html" # 
        icon = "media"
        label = "embeding"

class CardBlock(blocks.StructBlock):
    """ cards side by side with picture and text"""

    title = blocks.CharBlock(required=False, help_text="Add your title")
    
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text_body", blocks.TextBlock(required=True, max_length=350)),
                ("local_page_button", blocks.PageChooserBlock(required=False, help_text="(optional) - this is priority button")),
                ("url_button", blocks.URLBlock(required=False, help_text="(optional) - button above used first")),
            ]
        )
    )
    class Meta:  # noqa
        template = "streams/cards_block.html" # 




class FreeCarouselBlock(blocks.StructBlock):
    """ Large carousel with optional headings """
    
    carousel_pages = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=False, max_length=25)),
                ("sub_title", blocks.TextBlock(required=False, max_length=50)),
            ]
        )
    )
    class Meta:  # noqa
        template = "streams/carousel_block.html" 
        icon ="image"


class AltLrgMediaBlock(blocks.StructBlock):
    """ Large media blocks (FEATURETTES) with optional heading"""

    mediaList = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("r_image", ImageChooserBlock(required=True, help_text="must be at least 445x445")),
                ("r_title", blocks.CharBlock(required=False)),
                ("r_sub_title", blocks.CharBlock(required=False, max_length = 20)),
                ("r_paragraph", blocks.TextBlock(required=False, min_length = 50, max_length =450)),
                ("l_image", ImageChooserBlock(required=True)),
                ("l_title", blocks.CharBlock(required=False)),
                ("l_sub_title", blocks.CharBlock(required=False)),
                ("l_paragraph", blocks.TextBlock(required=False, min_length = 50, max_length = 450, help_text="might look with less than 200 characters")),

            ]
        )
    )
    class Meta:  # noqa
        template = "streams/alt_lrg_media_block.html"
        icon ="image"


class LeftSmMediaBlock(blocks.StructBlock):
    """ @TODO description"""

    mediaList = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True)),
                ("paragraph", blocks.TextBlock(required=True)),
            ]
        )
    )
    class Meta:  # noqa
        template = "streams/left_sm_media_block.html" 
        icon ="image"

class AltSmMediaBlock(blocks.StructBlock):
    """ @TODO description"""

    mediaList = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("r_image", ImageChooserBlock(required=True)),
                ("r_title", blocks.CharBlock(required=False, max_length = 20)),
                ("r_paragraph", blocks.TextBlock(required=False, min_length = 50, max_length = 250)),
                ("l_image", ImageChooserBlock(required=True)),
                ("l_title", blocks.CharBlock(required=False)),
                ("l_paragraph", blocks.TextBlock(required=False, min_length = 150, max_length = 350, help_text="Looks bad without at least 200 characters")),

            ]
        )
    )
    class Meta:  # noqa
        template = "streams/alt_sm_media_block.html"
        icon ="image"


# class WideBannerImageBlock(blocks.StructBlock):
#     # @TODO make template
#     ("image", ImageChooserBlock(required=True)),
#     ("title", blocks.CharBlock(required=False, max_length=25)),
#     ("sub_title", blocks.TextBlock(required=False, max_length=50)),

#     class Meta:  # noqa
#         template = "streams/basic_block.html" 
#         icon ="image"

# class SquareBannerImageBlock(blocks.StructBlock):
#     # @TODO make template
#     ("image", ImageChooserBlock(required=True)),
#     ("title", blocks.CharBlock(required=False, max_length=25)),
#     ("sub_title", blocks.TextBlock(required=False, max_length=50)),

#     class Meta:  # noqa
#         template = "streams/basic_block.html" 
#         icon ="image"




# class LinkStructValue(blocks.StructValue):
#     """Additional logic for our urls."""

#     def url(self):
#         button_page = self.get('button_page')
#         button_url = self.get('button_url')
#         if button_page:
#             return button_page.url
#         elif button_url:
#             return button_url

#         return None

#     # def latest_posts(self):
# #     return BlogDetailPage.objects.live()[:3]

# class ButtonBlock(blocks.StructBlock):
#     """An external or internal URL."""

#     button_page = blocks.PageChooserBlock(required=False, help_text='If selected, this url will be used first')
#     button_url = blocks.URLBlock(required=False, help_text='If added, this url will be used secondarily to the button page')

#     # def get_context(self, request, *args, **kwargs):
#     #     context = super().get_context(request, *args, **kwargs)
#     #     context['latest_posts'] = BlogDetailPage.objects.live().public()[:3]
#     #     return context

#     class Meta:  # noqa
#         template = "streams/button_block.html"
#         icon = "placeholder"
#         label = "Single Button"
#         value_class = LinkStructValue







# class NavDropList(blocks.StructBlock):
#     """ cards side by side with picture and text"""
#     title = blocks.CharBlock(required=True, max_length=12, help_text="Add your title")
#     drop_list = blocks.ListBlock(
#         blocks.StructBlock(
#             [
#                 ("nav_title", blocks.CharBlock(required=True, max_length=12)),
#                 ("nav_link", blocks.PageChooserBlock(required=True, help_text="choose a page to link to")),
#             ]
#         )
#     )
#     class Meta:  # noqa
#         template = "blocks/nav_drop_list.html" # 
#         icon = "arrow-down"


# class NavLink(blocks.StructBlock):
#     """ cards side by side with picture and text"""
#     title = blocks.CharBlock(required=True, max_length=12, help_text="Add your title"),
#     nav_link = blocks.PageChooserBlock(required=True, help_text="choose a page to link to"),

#     class Meta:  # noqa
#         template = "blocks/nav_title_link.html" # 
#         icon ="redirect"