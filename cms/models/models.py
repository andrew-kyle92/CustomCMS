from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.


class CacheTable(models.Model):
    cache_key = models.CharField(max_length=100, null=False)
    value = models.TextField(max_length=255, null=False)
    expires = models.DateTimeField('date', null=False)


class Page(models.Model):
    title = models.CharField(max_length=200)
    url = models.SlugField(unique=True,)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.url == "home":
            return reverse("index")
        else:
            return reverse("page_detail", kwargs={"url": self.url})


class Media(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='media/')
    created_at = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.page}"


class Post(models.Model):
    content = RichTextField()
