import re
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from users.models import CustomUser
from .serializers import CustomUserSerializer

from .tasks import multiply_by_ten

from .serializers import CelerySerializer

from rest_framework.response import Response

# Create your views here.


class UsersList(ListAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

class MultiTen(APIView):
    serializer_class = CelerySerializer

    def post(self, request):
        serializer = CelerySerializer(data=request.data)
        if serializer.is_valid():
            num = serializer.validated_data.get('number')
            new_num = multiply_by_ten.delay(num)
            return Response({'response':new_num})
