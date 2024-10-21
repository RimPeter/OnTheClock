from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from employee.forms import EmployeeForm
from employee.models import Employee

@login_required
def main(request):
    return render(request, 'main/main.html')

def pageserror404(request):
    return render(request, 'main/pages-error-404.html')

def pagesfaq(request):
    return render(request, 'main/pages-faq.html')

# def pageslogin(request):
#     return render(request, 'main/pages-login.html')

class CustomLoginView(auth_views.LoginView):
    template_name = 'main/pages-login.html'

    def form_valid(self, form):
        remember_me = self.request.POST.get('remember', None)
        if remember_me:
            # Session expires when the browser closes
            self.request.session.set_expiry(0)
        else:
            # Session expires in two weeks
            self.request.session.set_expiry(1209600)
        return super().form_valid(form)

def pagesregister(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('main')  
    else:
        form = RegisterForm()
    return render(request, 'main/pages-register.html', {'form': form})


@login_required
def usersprofile(request):
    try:
        employee = request.user.employee
    except Employee.DoesNotExist:
        return redirect('employee:create_profile')

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('main:users-profile')
    else:
        form = EmployeeForm(instance=employee)

    context = {
        'employee': employee,
        'form': form,
    }
    return render(request, 'main/users-profile.html', context)