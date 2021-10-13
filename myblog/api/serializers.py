from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from myblog.models import Post


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            # 'id',

            'title',
            'title_tag',
            'body',
            'post_date',
            'category',

        ]


class PostListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='api:api_detail')
    delete_url = HyperlinkedIdentityField(view_name='api:api_delete')
    update_url = HyperlinkedIdentityField(view_name='api:api_update')
    class Meta:

        model = Post
        fields = [
            'url',
            'delete_url',
            'update_url',
            'author',
            'title',
            'title_tag',
            'body',
            'post_date',
            'category',

        ]


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [

            'title',
            'title_tag',
            'body',
            'post_date',
            'category',

        ]


"""
data = {
        "title":"Yeahh buddy",
        "body":"New content",
        "category":"programming",
        "title_tag":"yeadd-ddd",
        "post_date":"2021-10-10",
        "author":1
        }
        
new_item = PostDetailSerializer(obj,data=data)
if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)
"""
