from django.urls import path
from .views import user_register, profile_view, edit_profile, follow_user, unfollow_user, user_list

urlpatterns = [
    path('', user_list, name='user_list'),
    path('register/', user_register, name='register'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('follow/<str:username>/', follow_user, name='follow_user'),
    path('unfollow/<str:username>/', unfollow_user, name='unfollow_user'),
]
