#coding=utf8
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from django.views.generic import ListView,DetailView,View

from music_player import files 
from .models import Article,Tag
from .content_parser import convert_all


#import markdown2

class ArticleListView(ListView):
    model = Article
    ordering = ['author','-published_date',]
    template_name = "posts.html"
    context_object_name = "posts"
    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ArticleDetailView(DetailView):
    model = Article
    template_name = "post.html"
    context_object_name = "post"
    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['zz'] = Tag.objects.all()
        return context

# def refresh(request):
#     convert_all(request.user)
#     return posts(request)

def mainpage(request):
    'render mainpage'
    articles = list(reversed(Article.objects.order_by('published_date')))
    musics = files.full_paths()

    import random
    music = random.choice(musics)

    context =\
    {
        'song_audio_file_url': music,
        'latest' : articles[0],
        'others' : articles[1:]
    }
    return render(request, 'main_page.html', context)


def search(request):
    q = request.GET.get('q', '')

    if q.startswith("GrandOrder:"):
        print q
        order = q[11:]
        print order
    return ArticleListView.as_view()(request)



