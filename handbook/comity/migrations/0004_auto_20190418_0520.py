# Generated by Django 2.1.2 on 2019-04-17 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comity', '0003_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='jecc_code',
            field=models.CharField(default='JEC', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='comity',
            name='comity_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='members',
            name='Member_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='members',
            name='designation',
            field=models.CharField(max_length=200),
        ),
    ]
