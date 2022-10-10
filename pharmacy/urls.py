from django.urls import path
from . import views

urlpatterns = [
    path('my-home/', views.ph_home, name='pharm-home') 
]