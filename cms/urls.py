from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path(r'^django-admin/', admin.site.urls),
    path('page/<slug:url>/', views.page_detail, name='page_detail'),
    path('', views.home_page, name='index'),
    re_path(r'^api/pages/', views.PageList.as_view(), name='page-list'),
    re_path(r'^api/pages/<int:pk>/', views.PageDetail.as_view(), name='page-data'),
    re_path(r'^api/tags/', views.PageList.as_view(), name='tags-list'),
    re_path(r'^api/tags/<int:pk>/', views.PageDetail.as_view(), name='tags-data'),
    re_path(r'^api/media/', views.PageList.as_view(), name='media-list'),
    re_path(r'^api/media/<int:pk>/', views.PageDetail.as_view(), name='media-data'),
    re_path(r'^api/comments/', views.PageList.as_view(), name='comments-list'),
    re_path(r'^api/comments/<int:pk>/', views.PageDetail.as_view(), name='comments-data'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



