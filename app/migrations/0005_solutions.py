# Generated by Django 3.0.3 on 2020-03-18 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_settings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solutions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('problem_number', models.IntegerField()),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
