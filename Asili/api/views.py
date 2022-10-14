from rest_framework import viewsets
from api.models import User
from .serializers import UserSerializer

class UserViewsets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    