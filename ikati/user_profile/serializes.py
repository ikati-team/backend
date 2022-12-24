from rest_framework import serializers

from django.conf import settings
from user_profile.models import Profile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ['url', 'username', 'email',
                  'first_name', 'last_name', 'date_joined', 'profile']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'city', 'biography',
                  'skill', 'preference_role']
