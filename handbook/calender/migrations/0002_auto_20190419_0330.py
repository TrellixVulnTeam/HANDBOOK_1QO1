# Generated by Django 2.1.2 on 2019-04-18 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calender', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
            ],
        ),
        migrations.DeleteModel(
            name='Contacts',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
