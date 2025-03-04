# Generated by Django 5.0 on 2024-11-29 10:06

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0023_image_contact_number_image_facebook_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcourse',
            name='description',
            field=ckeditor.fields.RichTextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='subcourse',
            name='image',
            field=models.ImageField(blank=True, default='default_image.jpg', null=True, upload_to='covers/'),
        ),
        migrations.CreateModel(
            name='SubCourseImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Subcourse_images/')),
                ('image_alt', models.CharField(blank=True, max_length=250, null=True)),
                ('meta_keyword', models.TextField(blank=True, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=100, null=True)),
                ('youtube_link', models.CharField(blank=True, max_length=250, null=True)),
                ('facebook_link', models.CharField(blank=True, max_length=250, null=True)),
                ('instagram_link', models.CharField(blank=True, max_length=250, null=True)),
                ('meta_title', models.CharField(blank=True, max_length=250, null=True)),
                ('meta_description', models.CharField(blank=True, max_length=250, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='courses.subcourse')),
            ],
        ),
    ]
