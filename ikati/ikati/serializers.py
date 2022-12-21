from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

# class NotificationSerializer(serializers.Serializer):
#     recipient = PublicUserSerializer(User, read_only=True)
#     unread = serializers.BooleanField(read_only=True)
#     target = GenericNotificationRelatedField(read_only=True)