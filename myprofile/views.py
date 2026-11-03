from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .forms import ContactForm, SignUpForm
from .models import Experience, Project


def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "پیام شما ثبت شد. از اینکه تماس گرفتید سپاسگزارم.")
            return redirect("home")
        messages.error(request, "لطفاً اطلاعات فرم را بررسی کنید.")
    else:
        form = ContactForm()
    return render(request, "myprofile/home.html", {
        "contact_form": form,
        "projects": Project.objects.all(),
        "experiences": Experience.objects.all(),
    })


def signup_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = SignUpForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "حساب کاربری شما ساخته شد.")
        return redirect("home")
    return render(request, "myprofile/signup.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        messages.success(request, "با موفقیت وارد شدید.")
        return redirect("home")
    return render(request, "myprofile/login.html", {"form": form})
