from rest_framework import permissions, viewsets

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from team.models import Team, Invite
from team.serializers import TeamSerializer, CreateTeamSerializer, InviteSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(TeamViewSet, self).dispatch(*args, **kwargs)


class CreateTeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = CreateTeamSerializer
    permission_classes = [permissions.IsAuthenticated]

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(CreateTeamViewSet, self).dispatch(*args, **kwargs)

# class InviteViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#     @method_decorator(csrf_exempt)
#     def dispatch(self, *args, **kwargs):
#         return super(UserViewSet, self).dispatch(*args, **kwargs)

class CurrentUserInviteViewSet(viewsets.ModelViewSet):
    serializer_class = InviteSerializer

    def get_queryset(self):
        print(self.request.user)
        invites = Invite.objects.get(target=self.request.user)
        return invites
