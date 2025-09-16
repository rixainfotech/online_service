from django.conf import settings
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    upi_id = models.CharField(max_length=120, blank=True)
    utr_number = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return f"{self.user.username} profile"