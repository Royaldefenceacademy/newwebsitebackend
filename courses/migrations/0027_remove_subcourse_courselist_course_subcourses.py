# Generated by Django 5.0 on 2024-11-29 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0026_remove_course_subcourselist_subcourse_courselist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcourse',
            name='courseList',
        ),
        migrations.AddField(
            model_name='course',
            name='SubCourses',
            field=models.ManyToManyField(blank=True, related_name='courses', to='courses.subcourse'),
        ),
    ]
