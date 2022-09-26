from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *


class BlogHome(ListView):
    model = MainPageText
    template_name = 'blog/index.html'
    context_object_name = 'content'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


class Pages(ListView):
    model = Posts
    template_name = 'blog/pages.html'
    context_object_name = 'articles'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Статьи'
        return context


class AboutSiteContent(ListView):
    model = AboutSite
    template_name = 'blog/about.html'
    context_object_name = 'about'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О сайте'
        return context


def registration(request):
    return render(request, 'blog/registration.html', {'title': 'Регистрация'})


class WriteAutor(CreateView):
    form_class = WriteToAutorForm
    template_name = 'blog/write_to_author.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Связаться с автором'
        return context


def fotogallery(request):
    return render(request, 'blog/foto.html', {'title': 'Фотогаллерея'})


class ShowPost(DetailView):
    model = Posts
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        return context


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
