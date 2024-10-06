from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request, 'main/main.html')

def chartapexcharts(request):
    return render(request, 'main/chart-apexcharts.html')

def chartschartjs(request):
    return render(request, 'main/charts-chartjs.html')

def chartsecharts(request):
    return render(request, 'main/charts-echarts.html')

def componentsaccordions(request):
    return render(request, 'main/components-accordions.html')