from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from ..serializers.todo_serializer import TodoSerializer
from ..models.todo import Todo
from ..filters.todo_filter import TodoFilter


class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = TodoLimitOffsetPagination
    filter_class = TodoFilter

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = 'закрыто'
        self.perform_create(instance)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
