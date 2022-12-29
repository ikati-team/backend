from rest_framework import serializers

from team.models import Team, TeamMember, Invite

from user_profile.serializers import UserSerializer
from django.contrib.auth.models import User


class TeamMemberSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = TeamMember
        fields = ['team', 'role', 'user']


class CreateTeamSerializer(serializers.HyperlinkedModelSerializer):
    role = serializers.CharField(write_only=True)

    def get_member_ids(self, team):
        out = []
        for i in TeamMember.objects.filter(team=team):
            out.append(i.id)
        return out

    def create(self, validated_data):
        team = Team(
            name=validated_data['name'],
            description=validated_data['public_message'],
            public_message=validated_data['public_message'],
        )
        team.save()
        TeamMember(user=self.context.get('request').user, team=team, role=validated_data['role']).save()

        return team

    class Meta:
        model = Team
        fields = ['id', 'name', 'public_message', 'role']


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    team_member = TeamMemberSerializer(many=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'public_message', 'team_member']


class InviteSerializer(serializers.HyperlinkedModelSerializer):
    target = UserSerializer
    team = TeamSerializer

    class Meta:
        model = Invite
        fields = ['target', 'team']
