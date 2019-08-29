from django.contrib import admin

from .models import CModel

class cAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titleC',)}

admin.site.register(CModel, cAdmin)