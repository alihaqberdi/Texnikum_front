from django.shortcuts import render, get_object_or_404
from home.models import Video, VideoCategorie
from django.views import View
from django.core.paginator import Paginator


# Create your views here.

def IndexView(request):
    return render(request, 'index.html')

def VebinarView(request):
    return render(request, 'webinar.html')

def NotificationView(request):
    return render(request, 'notificate.html')

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

def XizmatView(request):
    return render(request, 'xizmat.html')

def XabarnomaView(request):
    return render(request, 'xabarnoma.html')


def VideoView(request):
    video = Video.objects.all()
    categor = VideoCategorie.objects.all()
    p = Paginator(video, 6)
    page = request.GET.get('page')
    video_page = p.get_page(page)
    context = {
        'video': video_page,
        'categor': categor
    }
    return render(request, 'video_index.html', context)


def CategoryVideoView(request, pk):
    categor = VideoCategorie.objects.all()
    cate = get_object_or_404(VideoCategorie, id=pk)
    video = Video.objects.filter(categorie=cate)
    p = Paginator(video, 6)
    page = request.GET.get('page')
    video_page = p.get_page(page)
    context = {
        'cate': cate,
        'video': video_page,
        'categor': categor
    }
    return render(request, 'video_index.html', context)


class DetailVideoView(View):
    def get(self, request, pk=None):
        video = get_object_or_404(Video, id=pk)
        link = str(video.link).split('https://youtu.be/')[-1]
        context = {
            'link': link,
            'video': video
        }
        return render(request, 'video_detail.html', context)
    def post(self,request):
        pass
