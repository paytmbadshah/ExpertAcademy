# Generated by Django 3.1.4 on 2021-02-28 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_data_profile_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=250)),
                ('user_email', models.CharField(max_length=250)),
                ('badge', models.CharField(blank=True, choices=[('silver', 'silver'), ('bronze', 'bronze'), ('gold', 'gold')], max_length=250, null=True)),
                ('status', models.CharField(blank=True, choices=[('success', 'success'), ('pending', 'pending')], max_length=250, null=True)),
            ],
        ),
    ]
