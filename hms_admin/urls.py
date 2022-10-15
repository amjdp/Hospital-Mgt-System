from django.urls import path
from . import views

app_name = 'hms_admin'

urlpatterns = [
    path('',views.admin_home,name='admin_home'),
    path('add_admin',views.add_admin,name='adm_add'),
    path('view_admin',views.view_admin,name='adm_view'),
    path('view_appointments',views.view_app,name='app_view'),
    path('view_report',views.view_report,name='view_report'),
    path('add_doctor',views.add_dr,name='add_dr'),
    path('view_doctor',views.view_dr,name='view_dr'),
    path('add_patient',views.add_pt,name='add_pt'),
    path('view_patient',views.view_pt,name='view_pt'),
    path('add_department',views.add_dt,name='add_dt'),
    path('view_department',views.view_dt,name='view_dt'),
    path('change_password',views.chg_pwd,name='chg_pwd'),
    path('admin_profile',views.adm_prof,name='prof'),
    path('admin_login',views.admin_login,name='login')
]