# Generated by Django 3.0.3 on 2020-03-19 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_settings_mark_view'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='open_enrollment',
            field=models.BooleanField(default=False),
        ),
    ]
