from django.shortcuts import render

# Create your views here.


def getProfile(request):
    return render(request,"cabinet/profile.html")