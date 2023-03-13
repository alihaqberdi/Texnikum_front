from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name ='user'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('Profile/', views.ProfileView, name='profile'),
    path('logout/', views.LogoutView, name='logout')
]
