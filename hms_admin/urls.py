from django.urls import path
from . import views

urlpatterns = [
    path('my-home/', views.admin_home, name='admin-home') 
]