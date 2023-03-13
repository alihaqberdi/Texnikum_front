from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from home.models import Video
from django.views import View



class LoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html')
    def post(self, request):
        return render(request)

def ProfileView(request):
    return render(request, 'profile.html')


def LogoutView(request):
    logout(request)
    return redirect('home:index')

