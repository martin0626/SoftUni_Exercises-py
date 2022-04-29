from django.urls import path

from RESTFrameworkDemo.api.views import HomeView, LikesCountView, LikeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('like_add/', LikeView.as_view(), name='like'),
    path('likes_count/', LikesCountView.as_view(), name='like'),
]
