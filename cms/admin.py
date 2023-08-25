from django.contrib import admin
from .models.models import *

# Register your models here.
# admin.site.register(Page)
admin.site.register(Tag)
admin.site.register(Media)
admin.site.register(Comment)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                "classes": ["wide", "extrapretty"],
                "fields": ["title", "url"],
            },
        ),
    ]
    readonly_fields = ["created_at", "updated_at"]
    prepopulated_fields = {"url": ("title", )}
