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

def employee_profile(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    return render(request, 'employee/users-profile.html', {'employee': employee})