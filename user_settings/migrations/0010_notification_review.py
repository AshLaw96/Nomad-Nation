# Generated by Django 4.2.17 on 2025-02-24 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0022_caravan_currency'),
        ('user_settings', '0009_alter_notification_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notifications', to='listings.review'),
        ),
    ]
