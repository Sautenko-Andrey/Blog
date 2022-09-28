from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    path('pages/', Pages.as_view(), name='pages'),
    path('about/', AboutSiteContent.as_view(), name='about'),
    path('registration/', registration, name='registration'),
    path('write_to_autor/', WriteAutor.as_view(), name='write_to_autor'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('antalya/', Antalya.as_view(), name='antalya'),
    path('kemer/', Kemer.as_view(), name='kemer'),
    path('marmaris/', Marmaris.as_view(), name='marmaris'),
    path('fethie/', Fethie.as_view(), name='fethie'),
    path('foto/', fotogallery, name='fotogallery'),
    path('sponsorship/',Sponsor.as_view(),name='sponsorship'),
]
