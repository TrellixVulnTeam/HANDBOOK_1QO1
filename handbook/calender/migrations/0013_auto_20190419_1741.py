# Generated by Django 2.1.2 on 2019-04-19 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calender', '0012_eventinfo_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventinfo',
            old_name='photos',
            new_name='photo',
        ),
    ]
