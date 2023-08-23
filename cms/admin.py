from django.contrib import admin
from .models.models import *

# Register your models here.
# admin.site.register(Page)
admin.site.register(Tag)
admin.site.register(Media)
admin.site.register(Comment)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
