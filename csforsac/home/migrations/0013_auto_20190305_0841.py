# Generated by Django 2.1.7 on 2019-03-05 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20190305_0824'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutpage',
            old_name='body',
            new_name='bodyj',
        ),
        migrations.RenameField(
            model_name='aboutpage',
            old_name='extra',
            new_name='extraj',
        ),
        migrations.RenameField(
            model_name='aboutpage',
            old_name='more',
            new_name='morej',
        ),
        migrations.RenameField(
            model_name='aboutpage',
            old_name='test_field',
            new_name='test_fieldj',
        ),
    ]