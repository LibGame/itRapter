from django.contrib import admin

# Register your models here.
from .models import Programs

class ProgramsAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Programs , ProgramsAdmin)


