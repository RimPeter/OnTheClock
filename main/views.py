from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request, 'main/main.html')

def chartapexcharts(request):
    return render(request, 'main/charts-apexcharts.html')

def chartschartjs(request):
    return render(request, 'main/charts-chartjs.html')

def chartsecharts(request):
    return render(request, 'main/charts-echarts.html')

def componentsaccordions(request):
    return render(request, 'main/components-accordions.html')

def componentsalerts(request):
    return render(request, 'main/components-alerts.html')

def componentsbadges(request):
    return render(request, 'main/components-badges.html')

def componentsbreadcrumbs(request):
    return render(request, 'main/components-breadcrumbs.html')

def componentsbuttons(request):
    return render(request, 'main/components-buttons.html')

def componentscards(request):
    return render(request, 'main/components-cards.html')

def componentscarousel(request):
    return render(request, 'main/components-carousel.html')

def componenntslistgroup(request):
    return render(request, 'main/components-list-group.html')

def componentsmodals(request):
    return render(request, 'main/components-modals.html')

def componentspagination(request):
    return render(request, 'main/components-pagination.html')

def componentsprogress(request):
    return render(request, 'main/components-progress.html')

def componentsspinners(request):
    return render(request, 'main/components-spinners.html')

def componentstabs(request):
    return render(request, 'main/components-tabs.html')

def componentstooltips(request):
    return render(request, 'main/components-tooltips.html')

def formseditors(request):
    return render(request, 'main/forms-editors.html')

def formselements(request):
    return render(request, 'main/forms-elements.html')

def formslayouts(request):
    return render(request, 'main/forms-layouts.html')

def formsvalidation(request):
    return render(request, 'main/forms-validation.html')

def iconsbootstrap(request):
    return render(request, 'main/icons-bootstrap.html')

def iconsboxicons(request):
    return render(request, 'main/icons-boxicons.html')

def iconsremix(request):
    return render(request, 'main/icons-remix.html')

def pagesblank(request):
    return render(request, 'main/pages-blank.html')

def pagescontact(request):
    return render(request, 'main/pages-contact.html')

def pageserror404(request):
    return render(request, 'main/pages-error-404.html')

def pagesfaq(request):
    return render(request, 'main/pages-faq.html')

def pageslogin(request):
    return render(request, 'main/pages-login.html')

def pagesregister(request):
    return render(request, 'main/pages-register.html')

def tablesdata(request):
    return render(request, 'main/tables-data.html')

def tablesgeneral(request):
    return render(request, 'main/tables-general.html')

def usersprofile(request):
    return render(request, 'main/users-profile.html')