from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, UserViewSet
from .views import CustomAuthToken


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', CustomAuthToken.as_view(), name='api-token-auth'),
]