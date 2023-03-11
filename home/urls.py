from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name ='home'

urlpatterns = [
    path('about/', views.AboutView, name='about'),
    path('contact/', views.ContactView, name='contact'),
    path('elements/', views.ElementsView, name='elements'),
    path('', views.IndexView, name='index'),
    path('news/', views.NewsView, name='news'),
    path('service/', views.ServiceView, name='service'),
    path('video-maslahatlar/', views.VideoView, name='video'),
    ]