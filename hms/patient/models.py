from django.db import models
from hospital.models import Hospital  
from datetime import datetime   

class Patient(models.Model):
    patient_name = models.CharField(max_length=100)
    dob = models.DateField()
    phone_number = models.CharField(max_length=10,unique=True)
    disease = models.CharField(max_length=100)
    appointed_doctor_name = models.CharField(max_length=100)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    patient_status = models.CharField(max_length=50, choices=[
        ('admitted', 'Admitted'),
        ('discharged', 'Discharged'),
        ('observation', 'In Observation')
    ])

    def __str__(self):
        return f"{self.patient_name} "

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Check if the patient is discharged
        if self.patient_status == 'discharged':
            # Create a VisitTrack instance
            VisitTrack.objects.create(patient=self, patient_phone_number=self, activity='OUT')
        else:
            # Create a VisitTrack instance for 'IN'
            VisitTrack.objects.create(patient=self, patient_phone_number=self, activity='IN')
 
    
    
    # @classmethod
    # def change_status(cls, patient_id, new_status):
    #     cls.objects.filter(pk=patient_id).update(patient_status=new_status)
    @classmethod
    def change_status(cls, patient_id, new_status):
        patient = cls.objects.get(pk=patient_id)
        # old_status = patient.patient_status

        # Update patient status
        cls.objects.filter(pk=patient_id).update(patient_status=new_status)

        # Create or update VisitTrack entry based on the new status
        if new_status == 'discharged':
            VisitTrack.objects.update_or_create(
                patient=patient,
                patient_phone_number=patient,
                activity='OUT',
                defaults={'date_time': datetime.now()}
            )
        else:
            VisitTrack.objects.update_or_create(
                patient=patient,
                patient_phone_number=patient,
                activity='IN',
                defaults={'date_time': datetime.now()}
            )
   
   
class VisitTrack(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='visit_tracks_patient')
    patient_phone_number = models.ForeignKey(Patient, to_field='phone_number', on_delete=models.CASCADE, related_name='visit_tracks_phone_number')
    date_time = models.DateTimeField(auto_now_add=True)
    activity = models.CharField(max_length=3, choices=[
        ('IN', 'IN'),
        ('OUT', 'OUT')
    ])
    
    unique_together = ('patient', 'patient_phone_number')
    
    def __str__(self):
        return f"{self.patient.patient_name} - {self.activity} - {self.date_time}"
    
    def save(self,*args,**kwargs):
        if self.patient.patient_status == 'discharged':
            self.activity = 'OUT'
        else:
            self.activity = 'IN'
        super().save(*args,**kwargs)
        


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['patient', 'date_time'], name='unique_patient_datetime')
        ]