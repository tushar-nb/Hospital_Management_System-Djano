from django.db import models

# Create your models here.

class Hospital(models.Model):
    hospitalName = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    department = models.CharField(max_length=100)
    disease = models.CharField(max_length=100)

    def __str__(self):
        return self.hospitalName
    
    @classmethod
    def delete_by_name(cls, name):
        cls.objects.filter(hospitalName=name).delete()