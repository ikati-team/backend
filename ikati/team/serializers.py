from rest_framework import serializers

from team.models import Team, TeamMember

from user_profile.serializers import UserSerializer


class TeamMemberSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = TeamMember
        fields = ['role', 'user']


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    team_member = TeamMemberSerializer(many=True)

    class Meta:
        model = Team
        fields = ['name', 'description', 'public_message', 'team_member']
