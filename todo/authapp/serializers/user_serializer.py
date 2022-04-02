from ..models.users import UserDRF
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserDRF
        fields = ['url', 'username', 'email', 'groups']
