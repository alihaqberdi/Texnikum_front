from django.shortcuts import render

# Create your views here.

def IndexView(request):
    return render(request, 'index.html')


def ContactView(request):
    return render(request, 'contact.html')


def ElementsView(request):
    return render(request, 'elements.html')


def AboutView(request):
    return render(request, 'about.html')


def NewsView(request):
    return render(request, 'news.html')


def ServiceView(request):
    return render(request, 'services.html')


def VideoView(request):
    return render(request, 'video_index.html')