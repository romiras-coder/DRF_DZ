from rest_framework import serializers
from ..models.project import Project
from authapp.serializers.user_serializer import UserSerializer


class ProjectsSerializer(serializers.ModelSerializer):
    # users = UserSerializer(many=True)
    # user_created = UserSerializer()

    class Meta:
        model = Project
        fields = '__all__'
