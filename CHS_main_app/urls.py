from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage_main_view, name='homepage'),
    path('Book_Doctor/', views.book_doctor_module_view, name='book_doctor'),
    path('Disease_Catalog/', views.disease_catalog_view, name='disease_catalog'),
    path('Event_Catalog/', views.event_catalog_view, name='event_catalog'),
    path('Homepage2/', views.homepage_accounts_view, name='homepage2'),
    path('Patient_Catalog/', views.patient_catalog_view, name='patient_catalog'),
    path('About_Us/', views.about_us_view, name='about_us'),
    path('Staff_Catalog/', views.staff_catalog_view, name='staff_catalog'),
]