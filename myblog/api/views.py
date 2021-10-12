from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     UpdateAPIView,
                                     DestroyAPIView,
                                     CreateAPIView,
                                     )
from myblog.models import Post
from .serializers import (PostListSerializer,
                          PostDetailSerializer,
                          PostCreateSerializer,
                          )
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

class PostCreateApiview(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class PostDetailApiview(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'post_id'


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'post_id'


class PostUpdateApiview(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'post_id'
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwner]

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostListSerializer
