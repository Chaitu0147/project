# appointments/views.py
from django.shortcuts import render, redirect
from .models import Doctor, Patient, Appointment


def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor.html', {'doctors': doctors})

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})

def book_appointment(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)

    if request.method == 'POST':
        patient_form = PatientForm(request.POST)
        if patient_form.is_valid():
            patient = patient_form.save()
            date = request.POST.get('date')
            time = request.POST.get('time')
            appointment = Appointment(doctor=doctor, patient=patient, date=date, time=time)
            appointment.save()
            return redirect('doctor_list')
    else:
        patient_form = PatientForm()

    return render(request, 'book_appointment.html', {'doctor': doctor, 'patient_form': patient_form})
