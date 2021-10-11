from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     UpdateAPIView,
                                     DestroyAPIView)
from myblog.models import Post
from .serializers import PostListSerializer, PostDetailSerializer


class PostDetailApiview(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'post_id'


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'post_id'

class PostUpdateApiview(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'post_id'


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
