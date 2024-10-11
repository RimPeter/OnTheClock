from django.urls import path
from . import views


app_name = 'employee'

urlpatterns = [
    path('create_profile/', views.create_employee_profile, name='create_employee_profile'),
    path('list/', views.employee_list, name='employee_list'),
    path('profile/<int:employee_id>/', views.employee_profile, name='employee_profile'),
]
