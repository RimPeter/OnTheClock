from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    profile_picture = forms.ImageField(required=False)
    
    class Meta:
        model = Employee
        exclude = ['user', 'created_at', 'updated_at']
