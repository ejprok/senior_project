"""" Custom blocks for stream fields"""

from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock # can we figure out how to embed youtube
from wagtail.images.blocks import ImageChooserBlock

class TitleAndSubtitle(blocks.StructBlock):
    """ Typical Header """

    title = blocks.CharBlock(required=False, help_text="Add your title")
    sub_title = blocks.CharBlock(required=False, help_text="Add your sub-title")
    class Meta:  # noqa
        template = "generic/title_and_text_block.html"
        icon = "edit"
        label = "Title and Subtitle"

class RichtextBlock(blocks.RichTextBlock):
    """ Richtext """

    class Meta:  # noqa
        template = "generic/basic_block.html" # basic and simple text block
        icon = "doc-full"
        label = "Full Richtext"


class LimitedRichtextBlock(blocks.RichTextBlock):
    """Richtext with only limited features."""

    def __init__(
        self, required=True, help_text=None, editor="default", features=None, **kwargs
    ):  # noqa
        super().__init__(**kwargs)
        self.features = ["bold", "italic", "link","ol", "ul","image","embed"]

    class Meta:  # noqa
        template = "generic/basic_block.html" # basic and simple text block
        icon = "edit"
        label = "Limited Richtext"

class EmbededBlock(EmbedBlock):
    """ use rich text stream field instead """

    class Meta:  # noqa
        template = "generic/basic_block.html" # same template as "richtext_block.html"
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
                ("url_button", blocks.URLBlock(required=False, help_text="(optional) - above button used first")),
            ]
        )
    )
    class Meta:  # noqa
        template = "generic/cards_block.html" # same template as "richtext_block.html"

class NavDropList(blocks.StructBlock):
    """ cards side by side with picture and text"""
    title = blocks.CharBlock(required=True, max_length=12, help_text="Add your title")
    drop_list = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("nav_title", blocks.CharBlock(required=True, max_length=12)),
                ("nav_link", blocks.PageChooserBlock(required=True, help_text="choose a page to link to")),
            ]
        )
    )
    class Meta:  # noqa
        template = "generic/nav_drop_list.html" 
        icon = "arrow-down"


class NavLink(blocks.StructBlock):
    """ cards side by side with picture and text"""
    title = blocks.CharBlock(required=True, max_length=12, help_text="Add your title"),
    nav_link = blocks.PageChooserBlock(required=True, help_text="choose a page to link to"),

    class Meta:  # noqa
        template = "generic/nav_title_link.html" 
        icon ="redirect"