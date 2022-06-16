from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def user_login(request):
    return HttpResponse("Here goes the Login View")

def user_signup(request):
    return HttpResponse("Here goes the SignUp View")

def user_logout(request):
    return HttpResponse("Logout...")