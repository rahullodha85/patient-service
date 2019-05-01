from django.db import models

# Create your models here.

class patient(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.email