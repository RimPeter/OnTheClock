from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_employee_profile, name='create_employee_profile'),
    path('list/', views.employee_list, name='employee_list'),
]
