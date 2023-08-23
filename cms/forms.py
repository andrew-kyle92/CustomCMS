from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from .models.models import Post


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        field = '__all__'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

