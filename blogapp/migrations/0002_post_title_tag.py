# Generated by Django 3.1.2 on 2020-10-14 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default="My Freakin' Awesome Blog", max_length=255),
        ),
    ]