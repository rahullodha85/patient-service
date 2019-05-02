import json

from django.core import serializers
from django.http import HttpResponse
from .models import patient
# Create your views here.

def opt(request):
    return HttpResponse("Django Unchained!")

def test(request):
    return HttpResponse("test")

def get_patient(request, patient_id):
    patients =patient.objects.filter(id = patient_id)
    data = serializers.serialize('json', patients)
    return HttpResponse(data, content_type = 'application/json')

def get_patient_by_email(request, patient_email):
    patients =patient.objects.filter(email = patient_email)
    data = serializers.serialize('json', patients)
    return HttpResponse(data, content_type = 'application/json')
