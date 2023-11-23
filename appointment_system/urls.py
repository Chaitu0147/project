"""appointment_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# doctor_booking/urls.py
# doctor_booking/urls.py
from django.contrib import admin
from django.urls import  path
from appointments.views import doctor_list
from appointments.views import patient_list
from appointments.views import book_appointment
from home.views import home,login,register


urlpatterns = [
    path('admin/', admin.site.urls),
    path('appointments/', doctor_list, name='doctor_list'),
    path('appointment/', patient_list, name='patient_list'),
    path('appointments/<int:doctor_id>/', book_appointment, name='book_appointment'),
    path('',home),
    path('templates/login.html',login),
    path('templates/register.html',register),
    path('templates/doctor.html',doctor_list),
    path('templates/patient.html',patient_list),
    path('templates/book_appointment.html',book_appointment),
]

    