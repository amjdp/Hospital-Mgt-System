from django.shortcuts import render

# Create your views here.
def p_home(request):
    return render(request,'patient/patient_home.html')

def appointment(request):
    return render(request,'patient/appointment.html')

def confirmation(request):
    return render(request,'patient/confirmation.html')

def online_booking(request):
    return render(request,'patient/online_booking.html')

def my_bookings(request):
    return render(request,'patient/my_bookings.html')

def prescriptions(request):
    return render(request,'patient/prescriptions.html')

def chpass(request):
    return render(request,'patient/change-password.html')

def dr_profile(request):
    return render(request,'patient/dr_profile.html')

def my_profile(request):
    return render(request,'patient/my-profile.html')



    