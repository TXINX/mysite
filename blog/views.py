from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from music_player import file_path
from .models import Article
from .content_parser import convert_all

def posts(request):
    articles = reversed(Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date'))
    return render(request, 'posts.html', {'posts': articles})

def post(request,index=-1):
    if index == -1:
        return 'what the hell?'
    article = get_object_or_404(Article, pk=index)
    return render(request, 'posts.html', {'posts' : [article,]})
def refresh(request):
    convert_all(request.user)
    return post_list(request)

def main_page(request):
    'render mainpage'
    articles = list(reversed(Article.objects.order_by('published_date')))
    musics = file_path.full_paths()

    import random
    music = random.choice(musics)

    context =\
    {
        'song_audio_file_url': music,
        'latest' : articles[0],
        'others' : articles[1:]
    }
    return render(request, 'main_page.html', context)
    #return HttpResponse(template.render(context, request))
