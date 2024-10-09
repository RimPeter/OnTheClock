from django.shortcuts import render, redirect
from .forms import EmployeeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Employee

@login_required
def create_employee_profile(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')  
    else:
        form = EmployeeForm()
    return render(request, 'employee/create_profile.html', {'form': form})


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee/employee_list.html', {'employees': employees})
