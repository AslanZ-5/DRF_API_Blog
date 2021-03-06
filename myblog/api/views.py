from django.db.models import Q
from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     UpdateAPIView,
                                     DestroyAPIView,
                                     CreateAPIView,
                                     )
from myblog.models import Post
from myblog.models import Comment
from .serializers import (PostListSerializer,
                          PostDetailSerializer,
                          PostCreateSerializer,
                          CommentSerializer,
                          )
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.filters import (
        SearchFilter,
        OrderingFilter
)
from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination

)
from .pagination import PostLimitPagination,PaginationNumber


class PostCreateApiview(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailApiview(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'pk'



class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    lookup_field = 'pk'



class PostUpdateApiview(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'pk'

    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner]

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class PostListAPIView(ListAPIView):
    serializer_class = PostListSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title','body','author__first_name','author__last_name','author__username']
    pagination_class = PaginationNumber
    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.all().order_by('-id')
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(body__icontains=query) |
                Q(author__first_name__icontains=query) |
                Q(author__last_name__icontains=query)
            ).distinct()
        return queryset_list


class PostCommentDetailAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentListAPIView(ListAPIView):
    serializer_class = CommentSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['name','body']
    pagination_class = PaginationNumber
    def get_queryset(self, *args, **kwargs):
        queryset_list = Comment.objects.all().order_by('-id')
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(body__icontains=query) |
                Q(author__first_name__icontains=query) |
                Q(author__last_name__icontains=query)
            ).distinct()
        return queryset_list