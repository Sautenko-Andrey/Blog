from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect

from .forms import *
from .models import *


# menu = ['О сайте', 'Кнопка 1', 'Кнопка 2', 'Кнопка 3']


def index(request):
    content=MainPageText.objects.all()
    return render(request, 'blog/index.html',
                  {'title': 'Главная страница', 'content':content})


def pages(request):
    articles = Posts.objects.all()
    return render(request, 'blog/pages.html', {'title': 'Статьи', 'articles': articles})


def about(request):
    return render(request, 'blog/about.html', {'title': 'О сайте'})


def categories(request):
    return HttpResponse('<h1>Статьи по категориям</h1>')


def registration(request):
    return render(request, 'blog/registration.html',{'title':'Регистрация'})


def write_autor(request):
    if request.method=='POST':
        form=WriteToAutorForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                WriteToAutor.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None,'Ошибув отправки сообщения.')
    else:
        form=WriteToAutorForm
    return render(request,'blog/write_to_author.html',{'form':form,'title':'Связаться с автором'})

def fotogallery(request):
    return render(request, 'blog/foto.html',{'title':'Фотогаллерея'})


def show_post(request, post_slug):
    post=get_object_or_404(Posts,slug=post_slug)
    context={
        'post':post,
        'title':post.title,
    }
    return render(request,'blog/post.html',context=context)

def antalya_info(request):
    return render(request, 'blog/antalya_info.html', {'title': 'О Анталии'})

def kemer_info(request):
    return render(request, 'blog/kemer_info.html', {'title': 'О Кемере'})

def marmaris_info(request):
    return render(request, 'blog/marmaris_info.html', {'title': 'О Мармарисе'})


def fethie_info(request):
    return render(request, 'blog/fethie_info.html', {'title': 'О Фетхие'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

