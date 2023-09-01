from django.urls import path
from .import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('addnew/', views.addnew, name='addnew'),
    path('newuser/', views.newuser, name='newuser'),
    path('viewstaff/', views.viewstaff, name='viewstaff'),
]