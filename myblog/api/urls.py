from django.urls import path, include
from myblog.api.views import ( PostListAPIView,
                               PostDetailApiview,
                               PostUpdateApiview,
                               PostDeleteAPIView

    )

urlpatterns = [
    path('', PostListAPIView.as_view(), name='api_list'),
    path('<post_id>/',PostDetailApiview.as_view(),name='api_detail'),
    path('<post_id>/delete',PostDeleteAPIView.as_view(),name='api_delete'),
    path('<post_id>/edit',PostUpdateApiview.as_view(),name='api_update')

]