from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.users_view import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]
