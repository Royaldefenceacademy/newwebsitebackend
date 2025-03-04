# Generated by Django 5.0 on 2025-01-28 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0017_seo_scripts"),
    ]

    operations = [
        migrations.CreateModel(
            name="FAQ",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.CharField(max_length=500)),
                ("answer", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name="topscroller",
            name="description",
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="topscroller", name="title", field=models.CharField(null=True),
        ),
    ]
