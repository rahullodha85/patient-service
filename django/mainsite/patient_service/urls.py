from django.urls import path

from . import views

urlpatterns= [
    path('', views.opt, name = 'index'),
    path('test/', views.test, name='test'),
    path('get-patient/<str:patient_id>/', views.get_patient, name = 'get-patient-by-patient-id'),
    path('get-patient-email/<str:patient_email>/', views.get_patient_by_email, name = 'get-patient-by-patient-email'),
]