from django.urls import path
from . import views
from .views import signup_view
from .views import login_view

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    
]
