from django.urls import path
from . import views

urlpatterns = [
    path('my-home/', views.rec_home, name='recp-home') 
]