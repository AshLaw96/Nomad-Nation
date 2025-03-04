# Generated by Django 4.2.17 on 2025-01-16 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_availability_caravan_available_dates'),
    ]

    operations = [
        migrations.AddField(
            model_name='availability',
            name='caravan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='availability_caravans', to='listings.caravan'),
        ),
        migrations.AddField(
            model_name='availability',
            name='is_available',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='caravan',
            name='available_dates',
            field=models.ManyToManyField(blank=True, related_name='available_to_caravans', to='listings.availability'),
        ),
    ]
