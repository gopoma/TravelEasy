from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def user_login(request):
    return HttpResponse("Here goes the Login View")

def user_signup(request):
    return render(request, "accounts/signup.html")

def user_logout(request):
    return HttpResponse("Logout...")