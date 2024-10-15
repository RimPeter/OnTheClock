from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Employee

@login_required
def create_employee_profile(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')  
    else:
        form = EmployeeForm()
    return render(request, 'employee/create_profile.html', {'form': form})


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee/employee_list.html', {'employees': employees})


@login_required
def employee_profile(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)

    # Ensure the logged-in user is viewing their own profile
    if request.user != employee.user:
        messages.error(request, "You do not have permission to view this profile.")
        return redirect('employee:employee_list')

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('employee:employee_profile', employee_id=employee_id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'employee/users-profile.html', {'employee': employee, 'form': form})
