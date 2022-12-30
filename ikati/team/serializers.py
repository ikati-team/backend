from rest_framework import serializers

from team.models import Team, TeamMember, Invite

from user_profile.serializers import UserSerializer


class TeamMemberSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = TeamMember
        fields = ['team', 'role', 'user']


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    team_member = TeamMemberSerializer(many=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'public_message', 'team_member']


class InviteSerializer(serializers.HyperlinkedModelSerializer):
    team = TeamSerializer()

    class Meta:
        model = Invite
        fields = ['team']
