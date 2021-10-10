from django.urls import path
from .views import (UserRegisterView,
                    UserEditView,
                    PasswordsChangeView,
                    password_success,
                    ShowProfilePageView,
                    EditProfilePageView,
                    )
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
    path('edit_profile/',UserEditView.as_view(),name='edit_profile'),
    path('password/',PasswordsChangeView.as_view(),name='change_password'),
    path('password/success',password_success,name='password_success'),
    path('<int:pk>/profile', ShowProfilePageView.as_view(), name='profile'),
    path('<int:pk>/editprofilepage/',EditProfilePageView.as_view(),name='edit_profile_page')
]