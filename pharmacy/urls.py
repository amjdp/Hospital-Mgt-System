from django.urls import path
from . import views

app_name = 'pharmacy'

urlpatterns = [
    path('my-home/', views.ph_home, name='pharm-home') 
]