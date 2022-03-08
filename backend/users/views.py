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

from .serializers import MyTokenObtainPairSerializer, RegisterSerializer, GetUserSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
    

from django.contrib.auth.models import User
from rest_framework import generics

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    
class GetUserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = GetUserSerializer
    
# def createRandomUsers(request):
#     # import faker
#     from faker import Faker

#     #import db
#     from users.models import Profile

#     fake = Faker()
#     Faker.seed(0)

#     for i in range(0-100):
#         random_profile = fake.simple_profile()
#         username = random_profile["username"]
#         email = random_profile["email"]
#         password = random_profile["ssn"]

#         username_entry = Profile.objects.create_user(username, password=password, email=email)
        
#         username_entry.save()


#     admin_user = Profile.objects.create_user("nicocaste", password="202425NICo**", email="nicolas@castellano.com")
#     admin_user.is_superuser = True
#     admin_user.is_staff = True
#     admin_user.save()
#     return HTTPResponse("<H1>Your users have been created</H1>")