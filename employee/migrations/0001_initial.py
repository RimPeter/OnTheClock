# Generated by Django 5.1.1 on 2024-10-09 13:54

import django.core.validators
import employee.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('middle_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Middle Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('national_insurance_number', models.CharField(max_length=9, unique=True, validators=[employee.models.validate_nin], verbose_name='National Insurance Number')),
                ('house_number', models.CharField(max_length=10, verbose_name='House Number')),
                ('street_name', models.CharField(max_length=100, verbose_name='Street Name')),
                ('postcode', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(message='Enter a valid UK postcode (e.g., SW1A 1AA).', regex='^[A-Z]{1,2}\\d[A-Z\\d]? \\d[A-Z]{2}$')], verbose_name='Postcode')),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Enter a valid UK phone number.', regex='^\\+?44?\\d{10,14}$')], verbose_name='Phone Number')),
                ('email_address', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator(message='Enter a valid email address.')], verbose_name='Email Address')),
                ('driving_licence_number', models.CharField(blank=True, max_length=16, null=True, verbose_name='Driving Licence Number')),
                ('bank_name', models.CharField(max_length=100, verbose_name='Bank Name')),
                ('account_number', models.CharField(max_length=8, validators=[employee.models.validate_account_number], verbose_name='Account Number')),
                ('sort_code', models.CharField(max_length=8, validators=[employee.models.validate_sort_code], verbose_name='Sort Code')),
                ('emergency_contact_name', models.CharField(max_length=60, verbose_name='Emergency Contact Name')),
                ('emergency_contact_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Enter a valid UK phone number for emergency contact.', regex='^\\+?44?\\d{10,14}$')], verbose_name='Emergency Contact Number')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
                'ordering': ['last_name', 'first_name'],
            },
        ),
    ]
