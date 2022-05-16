
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from blog import permissions, serializers
from blog.classes import CreateRetrieveUpdateDestroy
from blog.models import Post
from blog.permissions import IsAuthor
from blog.serializers import ListPostSerializer, PostSerializer


class UserList(generics.ListAPIView):
    """
    Users' list
    """
    queryset = User.objects.all()
    serializer_class = serializers.GetUserSerializer


class UserDetail(generics.RetrieveAPIView):
    """
    One user's info
    """
    queryset = User.objects.all()
    serializer_class = serializers.GetUserSerializer


class PostListView(generics.ListAPIView):
    """
    User's wall
    """
    serializer_class = ListPostSerializer

    def get_queryset(self):
        return Post.objects.filter(
            user_id=self.kwargs.get('pk')).select_related('user')


class PostView(CreateRetrieveUpdateDestroy):
    """
    Post's CRUD
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all().select_related('user')
    serializer_class = PostSerializer
    permission_classes_by_action = {'get': [AllowAny],
                                    'update': [IsAuthor],
                                    'destroy': [IsAuthor]}

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
