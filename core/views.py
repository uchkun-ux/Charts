# from multiprocessing import context
from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)

def example(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'examp.html', context)


# mustaqil ish boshi


def bar(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'bar.html', context)

def line(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'line.html', context)


def radar(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'radar.html', context)


def doughnut(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'doughnut.html', context)


def polar(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'polar.html', context)


def bubble(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'bubble.html', context)

def scatter(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'scatter.html', context)

def area(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'area.html', context)