# Generated by Django 3.0.4 on 2020-03-23 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_settings_marks_adnotation'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(default='', max_length=100)),
                ('news_date', models.DateTimeField()),
                ('news_shortcut', models.TextField()),
                ('news_full', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Solutions',
        ),
    ]
