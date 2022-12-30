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
    social_network = SocialNetworkSerializer(many=True)

    class Meta:
        model = Profile
        fields = ['city', 'biography', 'skill', 'social_network', 'preference_role']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name',
                  'email', 'profile']

class LiteUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id']

