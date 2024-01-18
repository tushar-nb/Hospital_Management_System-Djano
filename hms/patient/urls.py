from django.urls import path 
from patient import views 

urlpatterns = [
  path('',views.patient_index,name='patient_index'),
  path('patient/',views.patient_list,name='patient_list'),
  path('patient/add',views.add_patient,name='add_patient'),
  path('patient/visit/',views.patient_detail,name='patient_detail'),
  path('patient/change_status/<int:patient_id>',views.change_patient_status,name='change_patient_status')
]
