from django.shortcuts import render
from django.contrib.auth.models import User, Group
from blogging.models import Post, Category
from rest_framework import viewsets
from rest_framework import permissions
from mysite.quickstart.serializers import UserSerializer, GroupSerializer, PostSerializer, CategorySerializer


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer
	permission_classes = [permissions.IsAuthenticated]


class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all().order_by('-created_date')
	serializer_class = PostSerializer
	permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
	permission_classes = [permissions.IsAuthenticated]