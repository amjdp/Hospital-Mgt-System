from django.shortcuts import render

# Create your views here.
def ph_home(request):
    return render(request,'pharmacy/pharm_home.html')