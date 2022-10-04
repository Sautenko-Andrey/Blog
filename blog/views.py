from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import MutualContext


class BlogHome(MutualContext, ListView):
    """Class for main page"""
    model = MainPageText
    template_name = 'blog/index.html'
    context_object_name = 'content'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        mutual_context_dict = self.get_user_context(title='Главная страница')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))


class Pages(MutualContext, ListView):
    """Class where user can read all posts"""
    paginate_by = 6
    model = Posts
    template_name = 'blog/pages.html'
    context_object_name = 'articles'

    def get_queryset(self):
        """This method search post by their title"""
        query = self.request.GET.get('q')
        if query:
            return Posts.objects.filter(title__iregex=query)
        else:
            return Posts.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        mutual_context_dict = self.get_user_context(title='Статьи')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))


class AboutSiteContent(MutualContext, ListView):
    """Class for page About"""
    model = AboutSite
    template_name = 'blog/about.html'
    context_object_name = 'about'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        mutual_context_dict = self.get_user_context(title='О блоге')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))


class Registration(MutualContext, CreateView):
    """Class for registration form"""
    form_class = RegistrationForm
    template_name = 'blog/registration.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        mutual_context_dict = self.get_user_context(title='Регистрация')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(MutualContext, LoginView):
    """Class for user authentication"""
    form_class = LoginForm
    template_name = 'blog/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        mutual_context_dict = self.get_user_context(title='Авторизация')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class WriteAutor(LoginRequiredMixin, MutualContext, CreateView):
    """Class for feedback"""
    form_class = WriteToAutorForm
    template_name = 'blog/write_to_author.html'
    success_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        mutual_context_dict = self.get_user_context(title='Связаться с автором')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))


class ShowPost(FormMixin,MutualContext, DetailView):
    """Class for showing particular post"""
    model = Posts
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    form_class = CommentForm
    success_url = reverse_lazy('pages')

    def post(self,request,*args,**kwargs):
        form=self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object=form.save(commit=False)
        self.object.post=self.get_object()
        self.object.name = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        mutual_context_dict = self.get_user_context(title=context_dict['post'])
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))



class AddComment(View):
    """Class for comments"""
    def post(self,request,pk):
        form=CommentForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.post_id=pk
            form.save()
        return redirect('home')



class Antalya(MutualContext, ListView):
    '''Class for info about Antalya on main page'''
    model = City
    template_name = 'blog/antalya_info.html'
    context_object_name = 'antalya'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        mutual_context_dict = self.get_user_context(title='О Анталии')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))

    def get_queryset(self):
        return City.objects.filter(pk=1)


class Kemer(MutualContext, ListView):
    """Class for info about Kemer"""
    model = City
    template_name = 'blog/kemer_info.html'
    context_object_name = 'kemer'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        mutual_context_dict = self.get_user_context(title='О Кемере')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))

    def get_queryset(self):
        return City.objects.filter(pk=2)


class Marmaris(MutualContext, ListView):
    """Class for info about Marmaris"""
    model = City
    template_name = 'blog/marmaris_info.html'
    context_object_name = 'marmaris'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        mutual_context_dict = self.get_user_context(title='О Мармарисе')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))

    def get_queryset(self):
        return City.objects.filter(pk=3)


class Fethie(MutualContext, ListView):
    """Class about Fethie"""
    model = City
    template_name = 'blog/fethie_info.html'
    context_object_name = 'fethie'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        mutual_context_dict = self.get_user_context(title='О Фетхие')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))

    def get_queryset(self):
        return City.objects.filter(pk=4)


class Sponsor(MutualContext, ListView):
    """Class for donation page"""
    model = Sponsorship
    template_name = 'blog/sponsorship.html'
    context_object_name = 'sponsor'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        mutual_context_dict = self.get_user_context(title='Спонсорство')
        return dict(list(context_dict.items()) + list(mutual_context_dict.items()))


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
