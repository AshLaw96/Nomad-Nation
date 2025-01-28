# Generated by Django 4.2.17 on 2025-01-20 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_availability_caravan_availability_is_available_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='caravan',
            old_name='size',
            new_name='berth',
        ),
        migrations.RemoveField(
            model_name='availability',
            name='date',
        ),
        migrations.AddField(
            model_name='availability',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='availability',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
