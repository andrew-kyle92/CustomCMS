from django.shortcuts import render

from rest_framework import generics
from .models.models import Page, Tag, Media, Comment
from .serializers import PageSerializers, TagSerializers, MediaSerializers, CommentSerializers

from rest_framework.permissions import IsAuthenticated


# Create your views here.
def page_detail(request, page_id):
    page = Page.objects.get(pk=page_id)
    template = 'templates_app/page_detail.html'
    context = {
        'page': page,
    }
    return render(request, template, context)


class PageList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Page.objects.all()
    serializer_class = PageSerializers


class PageDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Page.objects.all()
    serializer_class = PageSerializers


class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Tag.objects.all()
    serializer_class = TagSerializers


class MediaList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Media.objects.all()
    serializer_class = MediaSerializers


class MediaDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Media.objects.all()
    serializer_class = MediaSerializers


class CommentList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
