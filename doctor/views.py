from django.shortcuts import render

# Create your views here.
def dr_home(request):
    return render(request,'doctor/doctor_home.html')

def dr_profile(request):
    return render(request,'doctor/dr_profile.html')