from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

def home(request):
    return render(request, 'ghostwriting.html')

def detail(request, id):
    post = get_object_or_404(Post, pk = id)
    return render(request, 'detail.html', {'post':post})

def board(request):
    post = Post.objects.all()
    return render(request, 'board.html', {'post', post})

