from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name = 'main'

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.CustomLoginView.as_view(template_name='main/pages-login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='main:login'), name='logout'),
    path('pages-register/', views.pagesregister, name='pages-register'),
    path('users-profile/', views.usersprofile, name='users-profile'),
    path('pages-error-404/', views.pageserror404, name='pages-error-404'),
    path('pages-faq/', views.pagesfaq, name='pages-faq'),
]