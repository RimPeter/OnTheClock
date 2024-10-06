from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('chart-apexcharts/', views.chartapexcharts, name='chart-apexcharts'),
    path('charts-chartjs/', views.chartschartjs, name='charts-chartjs'),
    path('charts-echarts/', views.chartsecharts, name='charts-echarts'),
    path('components-accordions/', views.componentsaccordions, name='components-accordions'),
]