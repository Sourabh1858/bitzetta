# Generated by Django 4.2.13 on 2024-07-21 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toi', '0003_remove_course_enrolled_student_course_syllabus_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='about_course',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]