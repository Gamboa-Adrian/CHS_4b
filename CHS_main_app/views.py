##from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import NotBaseModel


# Create your views here.
def test_view(request):
    test_list = NotBaseModel.objects.all().values()
    template = loader.get_template('List_Testing.html')
    context = {
        'test_list': test_list,
    }
    return HttpResponse(template.render(context, request))


def book_doctor_module_view(request):
    template = loader.get_template('Book_Doctor_Module.html')
    return HttpResponse(template.render())


def disease_catalog_view(request):
    template = loader.get_template('Disease_Catalog.html')
    return HttpResponse(template.render())


def event_catalog_view(request):
    template = loader.get_template('Event_Catalog.html')
    return HttpResponse(template.render())


#homepage after successful login
def homepage_accounts_view(request):
    template = loader.get_template('Homepage_Accounts.html')
    return HttpResponse(template.render())


def homepage_main_view(request):
    template = loader.get_template('Homepage_Main.html')
    return HttpResponse(template.render())


def patient_catalog_view(request):
    template = loader.get_template('Patient_Catalog.html')
    return HttpResponse(template.render())


def about_us_view(request):
    template = loader.get_template('SacredHeart_AboutUs.html')
    return HttpResponse(template.render())


def staff_catalog_view(request):
    template = loader.get_template('Staff_Catalog.html')
    return HttpResponse(template.render())
