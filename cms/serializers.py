from rest_framework import serializers
from .models.models import Page, Tag, Media, Comment


class PageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class MediaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
