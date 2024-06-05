from django.contrib import admin
from .models import publicaciones

class publicacionesAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha',)

# Register your models here.

admin.site.register(publicaciones, publicacionesAdmin)