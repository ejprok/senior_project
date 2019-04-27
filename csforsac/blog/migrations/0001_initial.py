# Generated by Django 2.0.13 on 2019-04-27 23:23

from django.db import migrations, models
import django.db.models.deletion
import streams.custom_blocks
import wagtail.contrib.routable_page.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailimages', '0001_squashed_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogFocusPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('custom_title', models.CharField(blank=True, help_text='Type in the title for the blog article title', max_length=100)),
                ('blog_summary', models.TextField(help_text='Type in the summary for this blog article', max_length=255, null=True)),
                ('content', wagtail.core.fields.StreamField([('title_and_Subtitle', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=False)), ('sub_title', wagtail.core.blocks.CharBlock(help_text='Add your sub-title', required=False))])), ('full_richtext', streams.custom_blocks.RichtextBlock()), ('limited_richtext', streams.custom_blocks.LimitedRichtextBlock()), ('embeding', streams.custom_blocks.EmbededBlock()), ('card_block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=False)), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(max_length=40, required=True)), ('text_body', wagtail.core.blocks.TextBlock(max_length=350, required=True)), ('local_page_button', wagtail.core.blocks.PageChooserBlock(help_text='(optional) - this is priority button', required=False)), ('url_button', wagtail.core.blocks.URLBlock(help_text='(optional) - button above used first', required=False))])))]))], blank=True, null=True)),
                ('article_image', models.ForeignKey(help_text='This image is scalled to 500 pixels tall', null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.routable_page.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='BlogListingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('custom_title', models.CharField(blank=True, help_text='type in the title for the blog listing page', max_length=100)),
                ('blog_listing_banner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]