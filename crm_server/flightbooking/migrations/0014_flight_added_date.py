# Generated by Django 2.2 on 2019-06-25 16:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flightbooking', '0013_auto_20190625_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]