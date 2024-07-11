from datetime import datetime

from django.shortcuts import render

from .models import Post

def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())
