# Generated by Django 4.2.17 on 2025-02-19 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0021_remove_caravan_is_favourite_caravan_favourites'),
    ]

    operations = [
        migrations.AddField(
            model_name='caravan',
            name='currency',
            field=models.CharField(default='GBP', max_length=3),
        ),
    ]
