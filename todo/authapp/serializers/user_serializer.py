from ..models.users import UserDRF
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDRF
        # fields = ['url', 'username', 'email', 'groups']
        # fields = '__all__'
        exclude = ('user_permissions',)
