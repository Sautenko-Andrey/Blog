from django.urls import path
from .views import *
urlpatterns =[
    path('',index,name='home'),
    path('pages/',pages,name='pages'),
    path('cats/',categories),
    path('about/',about,name='about'),
    path('registration/',registration,name='registration'),
    path('write_to_autor/',write_autor,name='write_to_autor'),
    path('post/<int:post_id>/',show_post, name='post'),
    path('antalya/',antalya_info,name='antalya'),
    path('kemer/',kemer_info,name='kemer'),
    path('marmaris/',marmaris_info,name='marmaris'),
    path('fethie/',fethie_info,name='fethie'),
    path('foto/',fotogallery,name='fotogallery'),
]