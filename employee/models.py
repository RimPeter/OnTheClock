from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator, EmailValidator, ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

def validate_nin(value):
    """
    Validates UK National Insurance Number (NIN) format.
    Typical format: Two letters, six digits, one letter (e.g., AB123456C)
    """
    nin_regex = RegexValidator(
        regex=r'^[A-CEGHJ-PR-TW-Z]{2}\d{6}[A-D]$',
        message=_('Enter a valid UK National Insurance Number (e.g., AB123456C).')
    )
    nin_regex(value)

def validate_sort_code(value):
    """
    Validates UK Sort Code format: 6 digits, optionally separated by hyphens.
    """
    sort_code_regex = RegexValidator(
        regex=r'^(\d{2}-?){3}$',
        message=_('Enter a valid Sort Code (e.g., 12-34-56).')
    )
    sort_code_regex(value)

def validate_account_number(value):
    """
    Validates UK Bank Account Number format: 8 digits.
    """
    if not value.isdigit() or len(value) != 8:
        raise ValidationError(_('Enter a valid 8-digit Bank Account Number.'))
    
def user_directory_path(instance, filename):
    return f'profile_pictures/user_{instance.id}/{filename}'

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    JOB_TITLE_CHOICES = [
        ('driver', 'Driver'),
        ('instore', 'Instore'),
        ('manager', 'Manager'),
        ('shift-runner', 'Shift Runner'),
    ]
    # Personal Information
    first_name = models.CharField(max_length=30, verbose_name=_('First Name'))
    middle_name = models.CharField(max_length=30, verbose_name=_('Middle Name'), blank=True, null=True)
    last_name = models.CharField(max_length=30, verbose_name=_('Last Name'))
    date_of_birth = models.DateField(verbose_name=_('Date of Birth'))
    national_insurance_number = models.CharField(
        max_length=9,
        unique=True,
        validators=[validate_nin],
        verbose_name=_('National Insurance Number')
    )
    
    # Address Information
    house_number = models.CharField(max_length=10, verbose_name=_('House Number'))
    street_name = models.CharField(max_length=100, verbose_name=_('Street Name'))
    postcode = models.CharField(
        max_length=8,
        validators=[
            RegexValidator(
                regex=r'^[A-Z]{1,2}\d[A-Z\d]? \d[A-Z]{2}$',
                message=_('Enter a valid UK postcode (e.g., SW1A 1AA).')
            )
        ],
        verbose_name=_('Postcode')
    )
    
    profile_picture = models.ImageField(
        upload_to=user_directory_path,
        default='default_images/apple-touch-icon.png',
        blank=True,
        null=True,
        verbose_name=_('Profile Picture')
    )
    
    job_title = models.CharField(
        max_length=20,
        choices=JOB_TITLE_CHOICES,
        default='instore',
        verbose_name=_('Job Title')
    )
    
    # Contact Information
    phone_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?44?\d{10,14}$',
                message=_('Enter a valid UK phone number.')
            )
        ],
        verbose_name=_('Phone Number')
    )
    email_address = models.EmailField(
        unique=True,
        validators=[EmailValidator(message=_('Enter a valid email address.'))],
        verbose_name=_('Email Address')
    )
    
    # Driving Licence
    driving_licence_number = models.CharField(
        max_length=16,
        blank=True,
        null=True,
        verbose_name=_('Driving Licence Number')
    )
    
    # Bank Details
    bank_name = models.CharField(max_length=100, verbose_name=_('Bank Name'))
    account_number = models.CharField(
        max_length=8,
        validators=[validate_account_number],
        verbose_name=_('Account Number')
    )
    sort_code = models.CharField(
        max_length=8,
        validators=[validate_sort_code],
        verbose_name=_('Sort Code')
    )
    
    # Emergency Contact
    emergency_contact_name = models.CharField(max_length=60, verbose_name=_('Emergency Contact Name'))
    emergency_contact_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?44?\d{10,14}$',
                message=_('Enter a valid UK phone number for emergency contact.')
            )
        ],
        verbose_name=_('Emergency Contact Number')
    )
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))
    
    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')
        ordering = ['last_name', 'first_name']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
