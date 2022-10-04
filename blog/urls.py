from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60) (BlogHome.as_view()), name='home'),
    path('pages/', cache_page(60) (Pages.as_view()), name='pages'),
    path('about/', cache_page(60)(AboutSiteContent.as_view()), name='about'),
    path('registration/', Registration.as_view(), name='registration'),
    path('login/',LoginUser.as_view(),name='login'),
    path('logout/',logout_user,name='logout'),
    path('write_to_autor/', WriteAutor.as_view(), name='write_to_autor'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('antalya/', cache_page(60)(Antalya.as_view()), name='antalya'),
    path('kemer/', cache_page(60)(Kemer.as_view()), name='kemer'),
    path('marmaris/', cache_page(60)(Marmaris.as_view()), name='marmaris'),
    path('fethie/', cache_page(60)(Fethie.as_view()), name='fethie'),
    path('sponsorship/',cache_page(60)(Sponsor.as_view()),name='sponsorship'),
]


