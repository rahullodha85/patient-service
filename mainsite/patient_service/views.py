from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def opt(request):
    return HttpResponse("Django Unchained!")

def test(request):
    return HttpResponse("test")