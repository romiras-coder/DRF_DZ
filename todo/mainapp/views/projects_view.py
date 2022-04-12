from rest_framework.viewsets import ModelViewSet
from ..serializers.projects_serializer import ProjectsSerializer
from ..models.project import Project


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer
