from django.shortcuts import render
from django.utils import timezone

from .models import Article
from .content_parser import convert_all

def post_list(request):
    articles = reversed(Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date'))
    return render(request, 'post_list.html', {'posts': articles})

def refresh(request):
    convert_all(request.user)
    return post_list(request)
