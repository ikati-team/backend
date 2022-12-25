from rest_framework import serializers

from django.contrib.auth.models import User
from user_profile.models import Profile, Skill, SocialNetwork


class SkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skill
        fields = ['name', 'description']


class SocialNetworkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = ['type', 'link']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    skill = SkillSerializer(many=True)
    social_networks = SocialNetworkSerializer

    class Meta:
        model = Profile
        fields = ['city', 'biography', 'skill', 'social_networks', 'preference_role']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'profile']
