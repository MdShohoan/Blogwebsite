# Generated by Django 3.1.2 on 2020-10-22 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0011_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile'),
        ),
    ]
