from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name ='user'

urlpatterns = [
    path('register/', views.UserSignupView, name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('profile/', views.ProfileView, name='profile'),
]