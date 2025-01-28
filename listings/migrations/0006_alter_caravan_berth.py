# Generated by Django 4.2.17 on 2025-01-20 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_rename_size_caravan_berth_remove_availability_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caravan',
            name='berth',
            field=models.CharField(choices=[('small', 'Two'), ('medium', 'Four'), ('large', 'Six')], max_length=10),
        ),
    ]
