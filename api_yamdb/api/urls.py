from rest_framework import routers

from django.urls import path, include
from rest_framework.authtoken import views

from api.views import (
    ReviewViewSet, CommentViewSet,
    TitleViewSet, CategoryViewSet,
    GenreViewSet, UsersViewSet)

pp_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register('titles', TitleViewSet, basename='titles')
router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register(
    r'titles/(?P<post_id>\d+)/reveiws', ReviewViewSet, basename='reviews'
)
router_v1.register(
    r'titles/(?P<post_id>\d+)/reveiws/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comments'
)
router_v1.register('users', UsersViewSet, basename='users')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/signup/', views.user_register, name='register'),
    path('v1/auth/token/', views.token_create, name='token'),
]
