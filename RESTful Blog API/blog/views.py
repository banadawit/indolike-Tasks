from django.db import models
from rest_framework import serializers, viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from .models import Post
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import PostSerializer, UserSerializer
from django.contrib.auth.models import User

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """
        Save the new post instance with the author set to the current user.

        Parameters:
        serializer (PostSerializer): The serializer instance containing the validated data.
        """
        serializer.save(author=self.request.user)
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

# Custom Authentication View
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token, created = Token.objects.get_or_create(user=request.user)
        return Response({'token': token.key, 'user_id': request.user.id, 'username': request.user.username})
