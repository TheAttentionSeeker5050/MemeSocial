# from rest_framework import viewsets
# from .serializers import UserCreateSerializer, UserLoginSerializer

# # import user model
# from django.contrib.auth.models import User

# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# # generic views and mixins
# from rest_framework import mixins
# from rest_framework import generics

# class UserSignupAPIView(mixins.CreateModelMixin,generics.GenericAPIView):
    
#     """Create a new user"""
#     serializer_class = UserCreateSerializer
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class UserLoginAPIView(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     """Log in a new user"""
    
#     serializer_class = UserLoginSerializer
#     queryset = User.objects.all()
    
#     lookup_field = "username"
#     lookup_url_kwarg = "user"

from .serializers import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
    

from django.contrib.auth.models import User
from rest_framework import generics

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    
