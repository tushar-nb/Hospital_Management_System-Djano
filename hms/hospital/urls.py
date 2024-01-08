from django.urls import path 
from hospital import views 

urlpatterns = [
  path('',views.hospital_index,name='hospital_index'),
  path('hospital/',views.hospital_list,name='hospital_list'),
  path('hospital/add',views.add_hospital,name='add_hospital'),
  path('hospital/delete/<str:hospital_name>',views.delete_hospital,name='delete_hospital')
]
