from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='com-home'),
    path('master_page', views.masterpg, name='master'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('departments/', views.dept, name='depts'),
    path('services/', views.service, name='services'),
    path('login/', views.login, name='login'),
    path('blog-sidebar/', views.blog_sidebar, name='blog-sb'),
    path('blog-single/', views.blog_single, name='blog-single'),
    path('dept-single/', views.dept_single, name='dept-single'),
    path('doctor-single/', views.doc_single, name='dr-single'),
    path('doctor/', views.doc, name='dr'),
    path('documentation/', views.documentation, name='doc') 
]