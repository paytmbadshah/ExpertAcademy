# Generated by Django 3.1.4 on 2021-02-19 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_auto_20210210_1734'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course_comment',
            old_name='course_name',
            new_name='course_id',
        ),
    ]
