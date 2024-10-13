from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'main'

urlpatterns = [
    path('', views.main, name='main'),
    path('chart-apexchart/', views.chartapexchart, name='chart-apexchart'),
    path('charts-chartjs/', views.chartschartjs, name='charts-chartjs'),
    path('charts-echarts/', views.chartsecharts, name='charts-echarts'),
    path('components-accordion/', views.componentsaccordion, name='components-accordion'),
    path('components-alerts/', views.componentsalerts, name='components-alerts'),
    path('components-badges/', views.componentsbadges, name='components-badges'),
    path('components-breadcrumbs/', views.componentsbreadcrumbs, name='components-breadcrumbs'),
    path('components-buttons/', views.componentsbuttons, name='components-buttons'),
    path('components-cards/', views.componentscards, name='components-cards'),
    path('components-carousel/', views.componentscarousel, name='components-carousel'),
    path('components-list-group/', views.componentslistgroup, name='components-list-group'),
    path('components-modal/', views.componentsmodal, name='components-modal'),
    path('components-pagination/', views.componentspagination, name='components-pagination'),
    path('components-progress/', views.componentsprogress, name='components-progress'),
    path('components-spinners/', views.componentsspinners, name='components-spinners'),
    path('components-tabs/', views.componentstabs, name='components-tabs'),
    path('components-tooltips/', views.componentstooltips, name='components-tooltips'),
    path('forms-editors/', views.formseditors, name='forms-editors'),
    path('forms-elements/', views.formselements, name='forms-elements'),
    path('forms-layouts/', views.formslayouts, name='forms-layouts'),
    path('forms-validation/', views.formsvalidation, name='forms-validation'),
    path('icons-bootstrap/', views.iconsbootstrap, name='icons-bootstrap'),
    path('icons-boxicons/', views.iconsboxicons, name='icons-boxicons'),
    path('icons-remix/', views.iconsremix, name='icons-remix'),
    path('pages-blank/', views.pagesblank, name='pages-blank'),
    path('pages-contact/', views.pagescontact, name='pages-contact'),
    path('pages-error-404/', views.pageserror404, name='pages-error-404'),
    path('pages-faq/', views.pagesfaq, name='pages-faq'),
    
    path('login/', views.CustomLoginView.as_view(template_name='main/pages-login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('pages-register/', views.pagesregister, name='pages-register'),
    path('tables-data/', views.tablesdata, name='tables-data'),
    path('tables-general/', views.tablesgeneral, name='tables-general'),
    path('users-profile/', views.usersprofile, name='users-profile'),
]