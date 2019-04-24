from django.urls import path

from . import views

urlpatterns= [
    path('', views.opt, name = 'index'),
    path('test/', views.test, name='test'),
]