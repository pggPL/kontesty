# Generated by Django 3.0.3 on 2020-03-18 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_user_marks'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='mark_view',
            field=models.BooleanField(default=False),
        ),
    ]