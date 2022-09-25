from django.contrib import admin
from .models import *


class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}


class MainPageTextAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'picture_1', 'picture_2', 'picture_3')


class SocialNetAdmin(admin.ModelAdmin):
    list_display = ('instagram', 'facebook', 'youtube')
    list_display_links = ('instagram', 'facebook', 'youtube')
    search_fields = ('instagram', 'facebook', 'youtube')


class WriteToAutorAdmin(admin.ModelAdmin):
    list_display = ('title', 'message', 'email')
    list_display_links = ('title',)
    search_fields = ('title', 'message', 'email')


admin.site.register(Posts, PostsAdmin)
admin.site.register(MainPageText, MainPageTextAdmin)
admin.site.register(SocialNet, SocialNetAdmin)
admin.site.register(WriteToAutor,WriteToAutorAdmin)
