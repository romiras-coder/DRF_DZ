from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from ..serializers.projects_serializer import ProjectsSerializer
from ..models.project import Project
from ..filters.project_filter import ProjectFilter


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer
    pagination_class = ProjectLimitOffsetPagination
    filter_class = ProjectFilter
