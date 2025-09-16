from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Profile
from django.conf import settings

def home(request):
    return render(request, "index.html")

def register(request):
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
            messages.success(request, "Account created.")
            return redirect("course-list")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})