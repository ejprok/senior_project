# Generated by Django 2.1.7 on 2019-02-24 05:30

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='extra',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
