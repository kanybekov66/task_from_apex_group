from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import HumanSerializer, UserSerializer, CreateHumanSerializer
from .models import Human
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class HumanViewSet(viewsets.ModelViewSet):
    serializer_class = HumanSerializer
    queryset = Human.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )


class CreateHumanViewSet(viewsets.ModelViewSet):
    serializer_class = CreateHumanSerializer
    queryset = Human.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
