# Generated by Django 2.1.7 on 2019-03-12 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('home', '0014_auto_20190305_0849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='body',
        ),
        migrations.DeleteModel(
            name='AboutPage',
        ),
    ]
