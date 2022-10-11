from django.urls import path
from . import views

app_name = 'hms_admin'

urlpatterns = [
    path('',views.admin_home,name='admin_home')
]