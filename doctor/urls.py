from django.urls import path
from . import views

app_name = 'doctor'

urlpatterns = [
    path('my-home/', views.dr_home, name='dr-home'), 
    path('profile/', views.dr_profile, name='dr-pro')
]