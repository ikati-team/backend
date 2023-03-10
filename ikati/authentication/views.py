from django.contrib.auth import login
from rest_framework import permissions
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

from . import serializers


class LoginView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = serializers.LoginSerializer(data=self.request.data,
                                                 context={'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)


class RegisterView(views.APIView):
    permission_classes = (permissions.AllowAny)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = serializers.LoginSerializer(data=self.request.data,
                                                 context={'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        return Response(None, status=status.HTTP_202_ACCEPTED)
