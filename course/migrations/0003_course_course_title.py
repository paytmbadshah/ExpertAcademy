# Generated by Django 3.1.4 on 2021-02-05 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_title',
            field=models.CharField(default=2, max_length=250),
            preserve_default=False,
        ),
    ]
