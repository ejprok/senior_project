# Generated by Django 2.1.7 on 2019-03-03 23:30

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('home', '0007_homepage_test_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', models.CharField(max_length=255)),
                ('test_field', models.CharField(blank=True, max_length=30)),
                ('extra', wagtail.core.fields.RichTextField(blank=True)),
                ('more', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
