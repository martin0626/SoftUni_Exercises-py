from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import serializers
from rest_framework import serializers
from rest_framework import generics
from rest_framework import views
from rest_framework.response import Response

from RESTFrameworkDemo.api.models import Likes


class HomeView(TemplateView):
    template_name = 'index.html'


class LikesCountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = ['like']


class LikeView(generics.CreateAPIView):
    serializer_class = LikesCountSerializers
    queryset = Likes.objects.all()

# class LikeView(views.APIView):
#     serializer_class = LikesCountSerializers
#     queryset = Likes.objects.all()
#
#     def get(self, request):
#         like = Likes(like=1)
#         like.save()
#         likes_count = Likes.objects.count()
#         return Response(likes_count)


class LikesCountView(generics.ListAPIView):
    serializer_class = LikesCountSerializers
    queryset = Likes.objects.all()
