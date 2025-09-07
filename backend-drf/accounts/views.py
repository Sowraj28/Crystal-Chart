from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[AllowAny]
    
class ProtectedView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        response={
            'status':'Request Was Successful'
        }
        return Response(response)