from django.shortcuts import render

# Create your views here.
def rec_home(request):
    return render(request,'receptionist/rec_home.html')