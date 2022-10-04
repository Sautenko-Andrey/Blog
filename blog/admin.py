from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create','get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title','slug','content','time_create','time_update','photo','get_html_photo','is_published')
    readonly_fields = ('time_create','time_update','get_html_photo',)
    save_on_top = True

    def get_html_photo(self,object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width=50>')

    get_html_photo.short_description='Картинка'



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


class AboutSiteAdmin(admin.ModelAdmin):
    list_display = ('title', 'content','my_phone','my_mail','facebook_link',
                    'instagram_link','youtube_link','linkedn_link')
    list_display_links = ('title',)
    search_fields = ('title', 'content')

class CityAdmin(admin.ModelAdmin):
    list_display = ('title','picture_1','picture_2','picture_3','show_or_hide')
    list_display_links = ('title',)
    search_fields = ('title',)

class SponsorshipAdmin(admin.ModelAdmin):
    list_display = ('title','content','card_1','card_2','card_3')
    list_display_links = ('title',)
    search_fields = ('title',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','post','body','created','active')
    list_display_links = ('post','body')
    search_fields = ('name','body')


admin.site.register(Posts, PostsAdmin)
admin.site.register(MainPageText, MainPageTextAdmin)
admin.site.register(SocialNet, SocialNetAdmin)
admin.site.register(WriteToAutor, WriteToAutorAdmin)
admin.site.register(AboutSite, AboutSiteAdmin)
admin.site.register(City,CityAdmin)
admin.site.register(Sponsorship,SponsorshipAdmin)
admin.site.register(Comment,CommentAdmin)

admin.site.site_title='Админ-панель блога'
admin.site.site_header='Админ-панель блога'