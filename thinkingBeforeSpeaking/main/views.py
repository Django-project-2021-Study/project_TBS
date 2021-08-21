from django.shortcuts import render

def home(request):
    return render(request, 'ghostwriting.html')

def detail(request):
    return render(request, 'detail.html')

def board(request):
    return render(request, 'board.html')
