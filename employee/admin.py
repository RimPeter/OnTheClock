from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email_address', 'phone_number')
    search_fields = ('first_name', 'last_name', 'email_address', 'national_insurance_number')
    list_filter = ('date_of_birth', 'bank_name')


