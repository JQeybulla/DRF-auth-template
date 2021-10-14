from django.shortcuts import render
from rest_framework.generics import ListAPIView

from users.models import CustomUser
from .serializers import CustomUserSerializer
# Create your views here.


class UsersList(ListAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
