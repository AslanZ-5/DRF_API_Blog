from django.urls import path, include
from myblog.api.views import ( PostListAPIView,
                               PostDetailApiview,
                               PostUpdateApiview,
                               PostDeleteAPIView,
                               PostCreateApiview,
                               CommentListAPIView,

    )
app_name = 'api'
urlpatterns = [
    path('', PostListAPIView.as_view(), name='api_list'),
    path('add/', PostCreateApiview.as_view()),
    path('<int:pk>/',PostDetailApiview.as_view(),name='api_detail'),
    path('<int:pk>/delete',PostDeleteAPIView.as_view(),name='api_delete'),
    path('<int:pk>/edit',PostUpdateApiview.as_view(),name='api_update'),
    path('comment/', CommentListAPIView.as_view(), name='add_comment'),


]