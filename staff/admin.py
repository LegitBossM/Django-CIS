from django.contrib import admin
from . models import *
# Register your models here.

class AddNewAdmin(admin.ModelAdmin):
    list_display = ('staffno', 'departselect', 'firstname', 'lastname', 'email', 'phone', 'qualification', 'address', 'genderselect', 'date', 'salary')
admin.site.register(AddNewStaff, AddNewAdmin)



class AddNewUserAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'username', 'password')
admin.site.register(AddNewUser, AddNewUserAdmin)