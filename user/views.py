from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from . import form as forms
from . import models
from .form import PatsientForm
from .models import Profile


# Create your views here.

def register_patsient_view(request):
    patsientForm = PatsientForm()
    context = {'form': patsientForm}
    if request.method == 'POST':
        patsientForm = PatsientForm(request.POST)
        if patsientForm.is_valid():
            user = patsientForm.save()
            user.password(user.password)
            user.save()
        return redirect('user:login')
    return render(request, 'registration/signup.html', context)



def UserSignupView(request):
    userform = forms.UserForm()
    context = {'usercreate': userform}
    if request.method == "POST":
        userform = forms.UserForm(request.POST)
        if userform.is_valid() and request.POST['confirm_password'] == request.POST['password']:
            user = userform.save()
            user.username = user.username.lower()
            user.set_password(user.password)
            user.save()
            messages.success(request,'muvaffaqiyatli ro\'yxatdan o\'tildi')
            return redirect('user:login')
        else:

            messages.error(request,'xato malumotlarni tekshiring')


    return render(request, 'registration/signup.html', context)


class UserLoginView(View):
    def get(self,request):
        return render(request, 'registration/login.html')
    def post(self, request):
        username = request.POST['username']
        print(username)
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:index')
        return render(request, 'registration/login.html')

def LogoutView(request):
    logout(request)
    return redirect('home:index')


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwards):
    if created:
        Profile.objects.create(
            user=instance
        )
    else:
        profi = Profile.objects.get(user=instance)
        profi.name = instance.first_name+' '+instance.last_name
        profi.username = instance.username
        profi.save()


@receiver(post_delete, sender=Profile)
def ProfileDelite(sender, instance, **kwargs):
    user = instance.user
    user.delete()


def ProfileView(request):
    product = request.user.profile
    context = {
        'profile': product
    }
    return render(request, 'profile.html', context)