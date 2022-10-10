from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'common/homepage.html')

def masterpg(request):
    return render(request,'common/index.html')

def about(request):
    return render(request,'common/about.html')

def contact(request):
    return render(request,'common/contact.html')

def dept(request):
    return render(request,'common/department.html')

def service(request):
    return render(request,'common/service.html')

def login(request):
    return render(request,'common/login.html')

def dept_single(request):
    return render(request,'common/department-single.html')

def doc_single(request):
    return render(request,'common/doctor-single.html')

def doc(request):
    return render(request,'common/hms_doctor.html')

def documentation(request):
    return render(request,'common/documentation.html')

def blog_sidebar(request):
    return render(request,'common/blog-sidebar.html')

def blog_single(request):
    return render(request,'common/blog-single.html')
