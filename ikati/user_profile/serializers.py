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


class CreateProfileSerializer(serializers.HyperlinkedModelSerializer):
    skill = SkillSerializer(many=True)
    social_network = SocialNetworkSerializer(many=True)

    class Meta:
        model = Profile
        fields = ['city', 'biography', 'skill', 'social_network', 'preference_role']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name',
                  'email', 'profile']


class CreateUserSerializer(serializers.HyperlinkedModelSerializer):
    # password = serializers.CharField()
    # username = serializers.CharField()

    def create(self, validated_data):
        user = User(username=validated_data['username'],
                    first_name=validated_data['first_name'],
                    last_name=validated_data['last_name'],
                    email=validated_data['email'],
                    password=validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password']


class LiteUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id']


class AllSkillsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']


class CreateUserProfileSerilizer(serializers.HyperlinkedModelSerializer):
    skill = AllSkillsSerializer(many=True)
    social_network = SocialNetworkSerializer(many=True)
    user = LiteUserSerializer()

    class Meta:
        model = Profile
        fields = ['user', 'city', 'biography', 'skill', 'social_network', 'preference_role']
