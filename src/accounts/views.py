from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def user_login(request):
    return render(request, "accounts/login.html")

def user_signup(request):
    if request.method == "POST":
        print(request.POST)
    return render(request, "accounts/signup.html")

def user_logout(request):
    return HttpResponse("Logout...")