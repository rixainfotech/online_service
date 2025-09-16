from django.conf import settings
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    short_desc = models.CharField(max_length=250, blank=True)
    duration_weeks = models.PositiveIntegerField(default=8)

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    upi_id = models.CharField(max_length=120)
    utr_number = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user.username} -> {self.course.title}"
