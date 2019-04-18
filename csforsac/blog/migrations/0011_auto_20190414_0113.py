# Generated by Django 2.1.7 on 2019-04-14 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190414_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogfocuspage',
            name='blog_summary',
            field=models.TextField(help_text='Type in the summary for this blog article', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='blogfocuspage',
            name='article_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image'),
        ),
    ]