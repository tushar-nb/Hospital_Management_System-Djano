from django.shortcuts import get_object_or_404, render, redirect
from .models import Patient
from .forms import PatientForm
from rest_framework.views import APIView
from rest_framework.response import Response

def patient_index(request):
    return render(request,'patient/patient.html')

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient/patient_list.html', {'patients': patients})

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'patient/add_patient.html', {'form': form})

def change_patient_status(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    if request.method == 'POST':
        new_status = request.POST.get('new_status')
        patient.patient_status = new_status
        patient.save()
        return redirect('patient_list')
    else:
        # Prepare a list of status choices for the dropdown
        status_choices = Patient._meta.get_field('patient_status').choices

        return render(request, 'patient/change_status_form.html', {'patient': patient, 'status_choices': status_choices})