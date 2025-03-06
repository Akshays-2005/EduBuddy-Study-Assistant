from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def REGISTER(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Email Already Exists!')
            return redirect('register')

        # Create user with email as username
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name  # Store name in first_name field
        user.save()

        messages.success(request, "Registration successful! You can now log in.")
        return redirect('register')

    return render(request, 'registration/register.html')


def DO_LOGIN(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page
        else:
            messages.error(request, 'Invalid Email or Password!')
            return redirect('register')

    return render(request, 'registration/register.html')


def DO_LOGOUT(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('register')
