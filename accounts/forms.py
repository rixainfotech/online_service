from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    upi_id = forms.CharField(max_length=120, required=False, label='Pay with this UPI ID')
    utr_number = forms.CharField(max_length=120, required=True, label='UTR Number')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "upi_id", "utr_number")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply a common CSS class to all fields for styling
        # Prefill UPI from settings if present
        if hasattr(settings, 'UPI_ID_DEFAULT') and settings.UPI_ID_DEFAULT:
            self.fields['upi_id'].initial = settings.UPI_ID_DEFAULT

        for name, field in self.fields.items():
            existing = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = (existing + ' input').strip()