# Generated by Django 4.2.16 on 2024-11-11 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0002_banner_description_banner_image_alt_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="banner",
            name="meta_keyword",
            field=models.TextField(blank=True, null=True),
        ),
    ]
