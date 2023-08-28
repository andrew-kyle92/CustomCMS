from django.shortcuts import render
from django.conf import settings

from rest_framework import generics
from .models.models import Page, Tag, Media, Comment
from .serializers import PageSerializers, TagSerializers, MediaSerializers, CommentSerializers

from core.utils.functions import get_pages

from rest_framework.permissions import IsAuthenticated


# Create your views here.
def home_page(request):
    page = Page.objects.get(url="home")
    template = 'theme/index.html'
    pages = get_pages()
    context = {
        'page': page,
        'pages': pages,
    }
    return render(request, template, context)


def page_detail(request, url):
    page = Page.objects.get(url=url)
    template = 'templates_app/page_detail.html'
    pages = get_pages()
    context = {
        'page': page,
        'pages': pages,
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
