from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(
            username=username,
            password=password
        )

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid credentials")
            return redirect("/auth/login")
    return render(request, "accounts/login.html")

def user_signup(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password_confirmation = request.POST["password_confirmation"]

        # To avoid the null=False CONSTRAINT
        if not first_name or not last_name or not username or not email or not password or not password_confirmation:
            messages.info(request, "Fill all the fields...")
            return redirect("/auth/signup")

        # Passwords have to match each other
        if password != password_confirmation:
            messages.info(request, "Passwords don't match...")
            return redirect("/auth/signup")

        if  User.objects.filter(username=username):
            messages.info(request, "Username taken...")
            return redirect("/auth/signup")

        if User.objects.filter(email=email).exists():
            messages.info(request, "Email taken...")
            return redirect("/auth/signup")

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