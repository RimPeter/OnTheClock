# Generated by Django 5.1.1 on 2024-10-09 15:26

import employee.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='job_title',
            field=models.CharField(choices=[('driver', 'Driver'), ('instore', 'Instore'), ('manager', 'Manager'), ('shift-runner', 'Shift Runner')], default='instore', max_length=20, verbose_name='Job Title'),
        ),
        migrations.AddField(
            model_name='employee',
            name='profile_picture',
            field=models.ImageField(blank=True, default='default_images/apple-touch-icon.png', null=True, upload_to=employee.models.user_directory_path, verbose_name='Profile Picture'),
        ),
    ]
