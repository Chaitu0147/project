# appointments/forms.py
from django import forms
from .models import Doctor, Patient

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialty']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'email']
