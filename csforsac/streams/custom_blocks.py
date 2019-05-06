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

class CenteredTitle(blocks.StructBlock):
    """ Typical Header """

    title = blocks.CharBlock(required=False, help_text="Add your title")
    sub_title = blocks.CharBlock(required=False, help_text="Add your sub-title")
    class Meta:  # noqa
        template = "streams/centered_title_block.html"
        icon = "edit"
        label = "Centered Title"


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
    """ cards side by side with picture, text, and optional buttons """

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

# class CardRow(blocks.StructBlock):
#     """ 3 cards side by side without buttons"""
    
#     card = blocks.ListBlock(
#         blocks.StructBlock(
#             [
#                 ("title_1", blocks.CharBlock(required=True, max_length=40)),
#                 ("text_body_1", blocks.TextBlock(required=True, max_length=375)),
#                 ("title_2", blocks.CharBlock(required=True, max_length=40)),
#                 ("text_body_2", blocks.TextBlock(required=True, max_length=375)),
#                 ("title_3", blocks.CharBlock(required=True, max_length=40)),
#                 ("text_body_3", blocks.TextBlock(required=True, max_length=375)),
#             ]
#         )
#     )
#     class Meta:  # noqa
#         template = "streams/card_row.html" #

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


class LrgLeftMediaBlock(blocks.StructBlock):
    """ Large media blocks (FEATURETTES) with optional heading, Image on left """

    left_featurette = blocks.StructBlock(
    [
        ("img", ImageChooserBlock(required=True)),
        ("title", blocks.CharBlock(required=False)),
        ("sub_title", blocks.CharBlock(required=False)),
        ("paragraph", blocks.TextBlock(required=False, min_length = 50, max_length = 350)),
    ])
    class Meta:  # noqa
        template = "streams/lrg_left_media_block.html"
        icon ="image"

class LrgRightMediaBlock(blocks.StructBlock):
    """ Large media block (FEATURETTE) with optional heading, Image on right """

    right_featurette = blocks.StructBlock(
    [
        ("img", ImageChooserBlock(required=True)),
        ("title", blocks.CharBlock(required=False)),
        ("sub_title", blocks.CharBlock(required=False)),
        ("paragraph", blocks.TextBlock(required=False, min_length = 50, max_length = 350)),
    ])
    class Meta:  # noqa
        template = "streams/lrg_right_media_block.html"
        icon ="image"

class SmRightMediaBlock(blocks.StructBlock):
    """ @TODO description """
    right_media = blocks.StructBlock(
    [
        ("img", ImageChooserBlock(required=True)),
        ("title", blocks.CharBlock(required=False)),
        ("paragraph", blocks.TextBlock(required=False, min_length = 50, max_length = 350)),
    ])
    
    class Meta:  # noqa
        template = "streams/sm_right_media_block.html"
        icon ="image"
        label = "Sm Right Leaning Media"

class SmLeftMediaBlock(blocks.StructBlock):
    """ @TODO description """
    left_media = blocks.StructBlock(
    [
        ("img", ImageChooserBlock(required=True)),
        ("title", blocks.CharBlock(required=False)),
        ("paragraph", blocks.TextBlock(required=False, min_length = 50, max_length = 350)),
    ])
                
    class Meta:  # noqa
        template = "streams/sm_left_media_block.html"
        icon ="image"
        label = "Sm Left Leaning Media"


class BannerWideImageBlock(blocks.StructBlock):
    """ @TODO description """
    banner = blocks.StructBlock(
        [
            ("image", ImageChooserBlock(required=True, help_text="requires a very wide image")),
            ("title", blocks.CharBlock(required=False, max_length=25)),
            ("sub_title", blocks.TextBlock(required=False, max_length=50)),
        ]
    )
    class Meta:  # noqa
        template = "streams/banner_wide_image_block.html" 
        icon ="image"
        label = "Full Width Banner"


class BannerSquareImageBlock(blocks.StructBlock):
    # @TODO make template
    square_banner = blocks.StructBlock(
        [
            ("image", ImageChooserBlock(required=True)),
            ("title", blocks.CharBlock(required=False, max_length=25)),
            ("sub_title", blocks.TextBlock(required=False, max_length=150)),
        ]
    )
    class Meta:  # noqa
        template = "streams/banner_square_image_block.html" 
        icon ="image"
        label = "Square Img Banner"


class StreamLists():
    """ This class holds generic lists of stream fields """

    header_list = [
        ("free_carousel", FreeCarouselBlock()),
        ("wide_banner", BannerWideImageBlock()),
        ("square_banner", BannerSquareImageBlock()),
    ]
    
    body_list = [
            ("centered_title", CenteredTitle()),
            ("left_title", TitleAndSubtitle() ),
            ("full_richtext", RichtextBlock()),
            ("limited_richtext", LimitedRichtextBlock()),
            ("right_featurettes", LrgRightMediaBlock()),
            ("left_featurettes", LrgLeftMediaBlock()),
            ("Sm_Right_Media", SmRightMediaBlock()),
            ("Sm_Left_Media", SmLeftMediaBlock()),
            ("cards", CardBlock()),
            ("embeding", EmbededBlock()),
        ]





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

