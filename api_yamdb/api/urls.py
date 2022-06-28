from rest_framework import routers
from django.urls import path, include
from rest_framework.authtoken import views
from api.views import (
    ReviewViewSet, CommentViewSet,
    TitleViewSet, CategoryViewSet,
    GenreViewSet, UserViewSet, user_register, token_create, )

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register('titles', TitleViewSet, basename='titles')
router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register(
    r'titles/(?P<titles_id>\d+)/reviews', ReviewViewSet, basename='reviews'
)
router_v1.register(
    r'titles/(?P<titles_id>\d+)/reviews/(?P<reviews_id>\d+)/comments',
    CommentViewSet, basename='comments'
)
router_v1.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/signup/', user_register, name='register'),
    path('v1/auth/token/', token_create, name='token'),
]
