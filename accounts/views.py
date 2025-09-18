from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.conf import settings

from .forms import RegisterForm
from .models import Profile

def home(request):
    return render(request, "index.html")

def register(request):
    """Handles user registration"""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            upi = form.cleaned_data.get("upi_id") or getattr(settings, 'UPI_ID_DEFAULT', '')
            Profile.objects.create(
                user=user,
                upi_id=upi,
                utr_number=form.cleaned_data["utr_number"],
            )
            login(request, user)
            messages.success(request, "Account created successfully. Welcome!")
            return redirect("course-list")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})

def login_view(request):
    """Custom login view with validation"""
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        # Check if username exists
        if not User.objects.filter(username__iexact=username).exists():
            messages.error(request, "User not found. Please register first.")
            return redirect("login")

        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, "Invalid username or password.")
            return redirect("login")

        # Successful login
        login(request, user)
        messages.success(request, f"Welcome back, {user.username}!")
        return redirect("course-list")

    return render(request, "registration/login.html")

def logout_view(request):
    """Logs out the user and redirects to home page"""
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("home")