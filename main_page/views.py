from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse

from music_player import file_path

from blog.models import Article

def main_page(request):
    #songs=get_object_or_404(Song)
    convert_all(request.user)
    template = loader.get_template('main_page.html')
    articles = list(reversed(Article.objects.order_by('published_date')))
    #latest = Article.objects.order_by('published_date')[0]
    musics = file_path.full_paths()
    print musics
    import random
    music = random.choice(musics)
    print music
    context = {
        'song_audio_file_url': music,
        'latest' : articles[0],
        'others' : articles[1:]

    }
    return HttpResponse(template.render(context, request))
