from rest_framework import routers

from django.urls import path, include

from api.views import ReviewViewSet, CommentViewSet

pp_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register(
    r'titles/(?P<post_id>\d+)/reveiws', ReviewViewSet, basename='reviews'
)
router_v1.register(
    r'titles/(?P<post_id>\d+)/reveiws/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comments'
)
