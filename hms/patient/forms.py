# forms.py
from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['patient_name', 'dob', 'disease', 'appointed_doctor_name', 'hospital', 'patient_status']
