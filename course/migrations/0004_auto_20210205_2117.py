# Generated by Django 3.1.4 on 2021-02-05 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_course_course_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_title',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
