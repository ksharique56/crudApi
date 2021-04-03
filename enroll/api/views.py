from enroll.models import User
from enroll.api.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
 queryset = User.objects.all()
 serializer_class = UserSerializer
 authentication_classes = [BasicAuthentication]
 permission_classes = [IsAuthenticatedOrReadOnly]