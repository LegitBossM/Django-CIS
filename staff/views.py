from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from . models import *
from django.contrib import messages
# from . forms import *


# Create your views here.
def home(request):
    return render(request, 'home.html')

def addnew(request):
    if request.method == 'POST':
        staffno = request.POST['staffno']
        departselect = request.POST['departselect']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        qualification = request.POST['qualification']
        address = request.POST['address']
        genderselect = request.POST['genderselect']
        date = request.POST['date']
        salary = request.POST['salary']
        savedata = AddNewStaff(staffno=staffno, departselect=departselect, firstname=firstname, lastname=lastname, email=email, phone=phone, qualification=qualification, address=address, genderselect=genderselect, date=date, salary=salary)
        savedata.save()
        messages.info(request, 'Staff Added Successfully')
    return render(request, 'addnew.html')




def newuser(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        username = request.POST['username']
        password = request.POST['password']
        savedata = AddNewUser(fullname=fullname, username=username, password=password)
        savedata.save()
        messages.info(request, 'Added Successfully')
    return render(request, 'newuser.html')

def viewstaff(request):
    stafflist = AddNewStaff.objects.filter()
    return render(request, 'viewstaff.html', {'stafflist': stafflist})
