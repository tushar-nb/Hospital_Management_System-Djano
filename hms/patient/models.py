from django.db import models

# Create your models here.
# models.py
from django.db import models
from hospital.models import Hospital  

class Patient(models.Model):
    patient_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    disease = models.CharField(max_length=100)
    appointed_doctor_name = models.CharField(max_length=100)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    patient_status = models.CharField(max_length=50, choices=[
        ('admitted', 'Admitted'),
        ('discharged', 'Discharged'),
        ('observation', 'In Observation')
    ])

    def __str__(self):
        return f"{self.patient_name} - {self.hospital.hospitalName}"

    @classmethod
    def change_status(cls, patient_id, new_status):
        cls.objects.filter(pk=patient_id).update(patient_status=new_status)