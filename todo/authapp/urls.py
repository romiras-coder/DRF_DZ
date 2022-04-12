from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.users_view import UserViewSet
from mainapp.views.todo_view import TodoViewSet
from mainapp.views.projects_view import ProjectViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('todo', TodoViewSet)
router.register('projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls))
]
