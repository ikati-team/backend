from rest_framework import permissions, viewsets

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from team.models import Team
from team.serializers import TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(TeamViewSet, self).dispatch(*args, **kwargs)
