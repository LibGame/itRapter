from django.contrib import admin

# Register your models here.
from .models import JarModel

class jarAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titleJar',)}


admin.site.register(JarModel,jarAdmin)