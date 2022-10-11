from django.urls import path
from . import views

app_name = 'patient'

urlpatterns = [
    path('home', views.p_home, name='phome'),
    path('appointment', views.appointment, name='appointment'),
    path('confirmation', views.confirmation, name='confirm'),
    path('online-booking', views.online_booking, name='online'),
    path('my-bookings', views.my_bookings, name='bookings'),
    path('my-prescriptions', views.prescriptions, name='prescriptions'),
    path('change-password', views.chpass, name='chg-pwd'),
    path('doctor-profile', views.dr_profile, name='dr-pro'),
    path('patient-profile', views.my_profile, name='my-pro')
]
