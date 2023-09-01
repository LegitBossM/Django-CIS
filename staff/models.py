from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AddNewStaff(models.Model):
    staffno = models.CharField(max_length=100)
    departselect = models.CharField(max_length=100)
    # departselect = models.ManyToManyField()
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    genderselect = models.CharField(max_length=100)
    # genderselect = models.ManyToManyField()
    date = models.DateField(auto_now_add=True)
    salary = models.CharField(max_length=100)



class AddNewUser(models.Model):
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)