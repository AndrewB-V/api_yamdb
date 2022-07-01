from rest_framework.routers import DefaultRouter, SimpleRouter

from django.urls import include, path

from .views import (AdminViewSet, APITokenCreate, APIUserCreate, APIUserData,
                    CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet)

router_v1 = SimpleRouter()
router = DefaultRouter()

app_name = 'api'

router.register(
    'api/v1/users',
    AdminViewSet
)
router_v1.register(
    'categories',
    CategoryViewSet,
    basename='сategories'
)
router_v1.register(
    'titles',
    TitleViewSet,
    basename='titles'
)
router_v1.register(
    'genres',
    GenreViewSet,
    basename='genres'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

VERSION_PARAM = 'api/v1'

urlpatterns = [
    path(f'{VERSION_PARAM}/', include(router_v1.urls)),
    path(f'{VERSION_PARAM}/auth/signup/', APIUserCreate.as_view()),
    path(f'{VERSION_PARAM}/auth/token/', APITokenCreate.as_view()),
    path(f'{VERSION_PARAM}/users/me/', APIUserData.as_view()),
    path('', include(router.urls)),
]
