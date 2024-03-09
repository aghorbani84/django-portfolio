from django.http import JsonResponse
from django.shortcuts import render
from myproject.forms import LoginForm, SignupForm
from django.contrib.auth import login
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'myprofile/home.html')
    
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return JsonResponse({"success": True, "redirect_url": "/welcome/"})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors})
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"success": True, "redirect_url": "/welcome/"})
        else:
            return JsonResponse({"success": False, "error": "Invalid username or password"})
    return render(request, 'accounts/login.html')
    
