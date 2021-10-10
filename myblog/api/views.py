from rest_framework.generics import ListAPIView
from myblog.models import Post


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
