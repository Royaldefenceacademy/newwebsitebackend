# Generated by Django 5.1.3 on 2024-11-19 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_subcourse_youtube_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
