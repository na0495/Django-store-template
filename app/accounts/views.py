from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializers import CustomTokenObtainPairSerializer, RegisterSerializer

# ------------------------
# Account Apis views  ---
# ------------------------


class CustomObtainTokenPairView(TokenObtainPairView):
    """This Api allow user to login, by providing username and password and creating for them a JWT token"""

    permission_classes = (AllowAny,)
    serializer_class = CustomTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    """Register view, which allow user to sign up and create a new account"""

    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
