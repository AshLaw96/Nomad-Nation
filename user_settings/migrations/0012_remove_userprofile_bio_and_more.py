# Generated by Django 4.2.17 on 2025-02-28 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_settings', '0011_notification_related_object_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_pic',
        ),
    ]
