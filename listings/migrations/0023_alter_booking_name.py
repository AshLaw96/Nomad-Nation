# Generated by Django 4.2.17 on 2025-02-25 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0022_caravan_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
