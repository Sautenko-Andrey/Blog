from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    path('pages/', Pages.as_view(), name='pages'),
    path('about/', AboutSiteContent.as_view(), name='about'),
    path('registration/', registration, name='registration'),
    path('write_to_autor/', WriteAutor.as_view(), name='write_to_autor'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('antalya/', antalya_info, name='antalya'),
    path('kemer/', kemer_info, name='kemer'),
    path('marmaris/', marmaris_info, name='marmaris'),
    path('fethie/', fethie_info, name='fethie'),
    path('foto/', fotogallery, name='fotogallery'),
]
