from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse

from .models import Song

def main_page(request):
    #songs=get_object_or_404(Song)
    template = loader.get_template('main_page2.html')
    context = {
        'song_audio_file_url':"{%static 'musics/you.mp3' %}"
    }
    return HttpResponse(template.render(context, request))
