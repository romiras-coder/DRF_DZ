from rest_framework import serializers
from ..models.todo import Todo
from authapp.serializers.user_serializer import UserSerializer
from .projects_serializer import ProjectsSerializer


class TodoSerializer(serializers.ModelSerializer):
    user_created = UserSerializer()
    project = ProjectsSerializer()

    class Meta:
        model = Todo
        fields = '__all__'
