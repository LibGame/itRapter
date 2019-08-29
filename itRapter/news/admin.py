from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.urls import path

from itRapter import settings
from .models import Articles, CommentModel

admin.site.site_header = 'Admin Dashboard'

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('date',)
    readonly_fileds = ('body_preview',)

    class Media:
        js = (
            '{0}js/jquery-1.10.2.min.js'.format(settings.STATIC_URL),
            '{0}js/jquery.expander.min.js'.format(settings.STATIC_URL),
            '{0}itRapter\MainPage\static\script.js'.format(settings.STATIC_URL),
            )


admin.site.register(Articles,ArticleAdmin)

