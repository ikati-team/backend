from rest_framework import serializers

from team.models import Team, TeamMember, Invite
from user_profile.serializers import UserSerializer, LiteUserSerializer


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


class LiteTeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ['id']


class CreateInviteSerializer(serializers.HyperlinkedModelSerializer):
    team = LiteTeamSerializer
    user = LiteUserSerializer
    role = serializers.CharField(max_length=100)

    def create(self, validated_data):
        invite = Invite(user=validated_data['user'], team=validated_data['team'], role=validated_data['role'])
        invite.save()
        return invite

    class Meta:
        model = Invite
        fields = ['team', 'user', 'role']


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


class CreateTeamMemberSerializer(serializers.HyperlinkedModelSerializer):
    team = LiteTeamSerializer()
    user = LiteUserSerializer()
    role = serializers.CharField(max_length=100)

    def create(self, validated_data):
        team_member = TeamMember(user=validated_data['user'], team=validated_data['team'], role=validated_data['role'])
        team_member.save()
        return team_member

    class Meta:
        model = TeamMember
        fields = ['team', 'role', 'user']


class InviteSerializer(serializers.HyperlinkedModelSerializer):
    team = TeamSerializer()

    class Meta:
        model = Invite
        fields = ['id', 'team']
