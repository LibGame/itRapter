from django.contrib import admin

from .models import DjangoModel

class djangoAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titleDjango',)}

admin.site.register(DjangoModel, djangoAdmin)