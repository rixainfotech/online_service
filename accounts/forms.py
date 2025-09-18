from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    upi_id = forms.CharField(
        max_length=120,
        required=False,
        label='Pay with this UPI ID',
        disabled=True  # keep this to make it non-editable
    )
    utr_number = forms.CharField(max_length=120, required=True, label='UTR Number')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "upi_id", "utr_number")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Prefill UPI from settings if present
        if hasattr(settings, 'UPI_ID_DEFAULT') and settings.UPI_ID_DEFAULT:
            self.fields['upi_id'].initial = settings.UPI_ID_DEFAULT

        # Add a CSS class to all fields
        for name, field in self.fields.items():
            existing = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = (existing + ' input').strip()

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Email is already registered.")
        return email

    def clean_utr_number(self):
        utr = self.cleaned_data.get('utr_number', '').strip()
        if len(utr) < 6:
            raise forms.ValidationError("Enter a valid UTR number.")
        return utr