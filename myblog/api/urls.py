from django.urls import path, include
from myblog.api.views import ( PostListAPIView,

    )

urlpatterns = [
    path('', PostListAPIView.as_view(), name='list'),
]