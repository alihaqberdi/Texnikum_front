from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name ='home'

urlpatterns = [
    path('about/', views.AboutView, name='about'),
    path('vebinar/', views.VebinarView, name='vebinar'),
    path('notification/', views.NotificationView, name='notificate'),
    path('Xabarnoma/', views.XabarnomaView, name='xabarnoma'),
    path('contact/', views.ContactView, name='contact'),
    path('Xizmat/', views.XizmatView, name='xizmat'),
    path('elements/', views.ElementsView, name='elements'),
    path('', views.IndexView, name='index'),
    path('news/', views.NewsView, name='news'),
    path('service/', views.ServiceView, name='service'),
    path('video-maslahatlar/', views.VideoView, name='video'),
    path('video-maslahatlar/<int:pk>/', views.DetailVideoView.as_view(), name='detail_video'),
    path('video-category/<int:pk>/', views.CategoryVideoView, name='category_video'),
    ]