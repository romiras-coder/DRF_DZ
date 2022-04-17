from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authapp.views.users_view import UserViewSet
from .views.todo_view import TodoViewSet
from .views.projects_view import ProjectViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('todo', TodoViewSet)
router.register('projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls))
]
