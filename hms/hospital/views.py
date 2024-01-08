from django.shortcuts import render,redirect
from .models import Hospital
from .forms import HospitalForm
from rest_framework.views import APIView
from rest_framework.response import Response

def hospital_index(request):
    return render(request,'hospital/hospital.html')

def hospital_list(request):
    hospitals = Hospital.objects.all()
    return render(request,'hospital/hospital_list.html',{'hospitals':hospitals})

def add_hospital(request):
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hospital_list')
    else:
        form = HospitalForm()
    return render(request, 'hospital/add_hospital.html', {'form': form})

def delete_hospital(request, hospital_name):
    Hospital.delete_by_name(hospital_name)
    return redirect('hospital_list')