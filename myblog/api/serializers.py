from rest_framework.serializers import ModelSerializer
from myblog.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'title',
            'title_tag',
            'body',
            'post_date',
            'category',

        ]
