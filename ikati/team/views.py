from rest_framework import permissions, viewsets

from team.models import Team, Invite, TeamMember
from team.serializers import TeamSerializer, CreateTeamSerializer, InviteSerializer, CreateInviteSerializer, CreateTeamMemberSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]


class CreateTeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = CreateTeamSerializer
    permission_classes = [permissions.IsAuthenticated]

class CreateTeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = CreateTeamMemberSerializer
    permission_classes = [permissions.IsAuthenticated]


class CurrentUserInviteViewSet(viewsets.ModelViewSet):
    serializer_class = InviteSerializer

    def get_queryset(self):
        print(self.request.user)
        invites = Invite.objects.filter(user=self.request.user)
        return invites


class CreateInviteViewSet(viewsets.ModelViewSet):
    serializer_class = CreateInviteSerializer
    queryset = set()
