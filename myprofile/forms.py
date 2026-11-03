from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import ContactMessage


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label="ایمیل")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ("name", "email", "subject", "message")
        labels = {
            "name": "نام شما",
            "email": "ایمیل",
            "subject": "موضوع",
            "message": "پیام",
        }
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "نام و نام خانوادگی", "autocomplete": "name"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@example.com", "autocomplete": "email"}),
            "subject": forms.TextInput(attrs={"placeholder": "موضوع پیام"}),
            "message": forms.Textarea(attrs={"placeholder": "درباره چیزی که در ذهن دارید بنویسید...", "rows": 5}),
        }
