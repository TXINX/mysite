from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    posts = reversed(Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date'))
    return render(request, 'post_list.html', {'posts': posts})
