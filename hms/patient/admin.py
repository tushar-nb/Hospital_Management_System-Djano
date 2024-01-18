from django.contrib import admin
from .models import Patient, VisitTrack
# Register your models here.
admin.site.register(Patient)
admin.site.register(VisitTrack)