# Generated by Django 2.1.2 on 2019-04-19 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calender', '0011_auto_20190419_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventinfo',
            name='thumbnail',
            field=models.ImageField(blank=True, editable=False, upload_to='thumbs'),
        ),
    ]
