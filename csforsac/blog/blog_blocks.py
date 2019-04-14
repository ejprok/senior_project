"""" Custom blocks for the blog page - inspired by (and with credit to)
https://github.com/CodingForEverybody/learn-wagtail/commit/84ad12e1b69343f192a44359ca0f7b19fe681ca7"""

from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock # can we figure out how to embed youtube


class TitleAndTextBlock(blocks.StructBlock):
    """ Typical Header """

    title = blocks.CharBlock(required=True, help_text="Add your title")
    sub_title = blocks.CharBlock(required=True, help_text="Add your sub-title")
    class Meta:  # noqa
        template = "blog/title_and_text_block.html"
        icon = "edit"
        label = "Title and Subtitle"

class RichtextBlock(blocks.RichTextBlock):
    """ Richtext """

    class Meta:  # noqa
        template = "blog/basic_block.html"
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
        template = "blog/basic_block.html" # same template as "richtext_block.html"
        icon = "edit"
        label = "Limited Richtext"

class EmbededBlock(EmbedBlock):
    """Richtext with only limited features."""

    class Meta:  # noqa
        template = "blog/basic_block.html" # same template as "richtext_block.html"
        icon = "media"
        label = "embeding"
