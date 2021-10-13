from rest_framework.serializers import (ModelSerializer,
                                        HyperlinkedIdentityField,
                                        SerializerMethodField,
                                        )
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
    detail = HyperlinkedIdentityField(view_name='api:api_detail')
    delete_url = HyperlinkedIdentityField(view_name='api:api_delete')
    update_url = HyperlinkedIdentityField(view_name='api:api_update')
    user = SerializerMethodField()


    class Meta:
        model = Post
        fields = [
            'detail',
            'delete_url',
            'update_url',
            'user',
            'title',
            'title_tag',
            'body',
            'post_date',
            'category',

        ]

    def get_user(self, obj):
        return str(obj.author.username)




class PostDetailSerializer(ModelSerializer):
    user = SerializerMethodField()
    delete_url = HyperlinkedIdentityField(view_name='api:api_delete')
    update_url = HyperlinkedIdentityField(view_name='api:api_update')

    class Meta:
        model = Post
        fields = [
            'delete_url',
            'update_url',
            'user',
            'title',
            'title_tag',
            'body',
            'post_date',
            'category',

        ]

    def get_user(self, obj):
        return str(obj.author.username)


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
