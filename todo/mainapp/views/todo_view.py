from rest_framework.viewsets import ModelViewSet
from ..serializers.todo_serializer import TodoSerializer
from ..models.todo import Todo


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
