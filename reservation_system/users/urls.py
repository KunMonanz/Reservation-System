from .views import (
    UserCreateView,
    ProfileView,
    UserLoginView
)
from django.urls import path

urlpatterns = [
    path(
        'v1/register/',
        UserCreateView.as_view(),
        name='user-register'
    ),
    path(
        'v1/profile/',
        ProfileView.as_view(),
        name='user-profile'
    ),
    path(
        'v1/login/',
        UserLoginView.as_view(),
        name='user-login'
    ),
]
