from typing import Set
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    #title - CharField max_length = 60
    title = models.CharField(max_length=128)
    #text - TextField
    text = models.TextField(blank=True)
    #author - CharField max_length = 30
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #created_date - DateField auto_now_add=False
    created_date = models.DateTimeField(auto_now_add=True)
    #modified_date - DateField auto_now=True
    modified_date = models.DateTimeField(auto_now=True)
    #published_date -  - DateField auto_now_add=True
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    #name
    name = models.CharField(max_length=128)
    #description
    description = models.TextField(blank=True)
    #posts
    posts = models.ManyToManyField(Post, blank=True, related_name='Categories')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'