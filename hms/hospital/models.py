from django.db import models

# Create your models here.
class Depratment(models.Model):
    department_name = models.CharField(max_length =50)
    
    def __str__(self):
        return self.department_name
    
class Hospital(models.Model):
    hospitalName = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    # departments = models.ManyToManyField(Depratment)
    departments = models.CharField(max_length=255)
    

    def __str__(self):
        return self.hospitalName
    
    @classmethod
    def delete_by_name(cls, name):
        cls.objects.filter(hospitalName=name).delete()