from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

# Create your views here.
def user_login(request):
    return render(request, "accounts/login.html")

def user_signup(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password_confirmation = request.POST["password_confirmation"]

        if password != password_confirmation:
            return HttpResponse("Passwords not matching...")

        if User.objects.filter(username=username):
            return HttpResponse("Username taken")

        if User.objects.filter(email=email).exists():
            return HttpResponse("Email taken")

        newUser = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        newUser.save()

        print("The user was CREATED", newUser)
        return redirect("/")
    return render(request, "accounts/signup.html")

def user_logout(request):
    return HttpResponse("Logout...")