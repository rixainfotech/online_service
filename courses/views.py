from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Enrollment


def course_list(request):
    courses = Course.objects.all().order_by('title')
    return render(request, "courses/course_list.html", {"courses": courses})


@login_required
def enroll(request, course_id: int):
    course = get_object_or_404(Course, id=course_id)
    profile = getattr(request.user, "profile", None)
    if not profile or not profile.upi_id or not profile.utr_number:
        messages.error(request, "Please provide UPI ID and UTR in your profile (from registration).")
        return redirect("course-list")
    Enrollment.objects.get_or_create(
        user=request.user,
        course=course,
        defaults={"upi_id": profile.upi_id, "utr_number": profile.utr_number},
    )
    messages.success(request, f"Enrolled in {course.title}.")
    return redirect("course-list")

# Create your views here.
