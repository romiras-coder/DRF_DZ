from rest_framework.viewsets import ModelViewSet
from ..models.users import UserDRF
from ..serializers.user_serializer import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = UserDRF.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'put', 'patch']
