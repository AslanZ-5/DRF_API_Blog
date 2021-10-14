from django.urls import path, include
from . import views
from .views import (HomeView,
                    BlogDetailView,
                    AddPostView,
                    UpdatePostView,
                    DeletePostView,
                    AddCategoryView,
                    CategoryView,
                    CategoryListView,
                    LikeView,
                    AddCommentView)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('post/add/', AddPostView.as_view(), name='add_post'),
    path('category/add/', AddCategoryView.as_view(), name='add_category'),
    path('post/update/<int:pk>/', UpdatePostView.as_view(), name='update_post'),
    path('post/delete/<int:pk>/', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category_list'),
    path('like/<int:pk>/', LikeView, name='like_post'),
    path('comment_add/post/<int:pk>', AddCommentView.as_view(), name='add_comment')

]
