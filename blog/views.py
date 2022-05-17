

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render


from rest_framework import generics, response, request
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from blog import permissions, serializers
from blog.classes import CreateRetrieveUpdateDestroy
from blog.forms import EmailPostForm
from blog.models import Post, Follower
from blog.permissions import IsAuthor
from blog.serializers import ListPostSerializer, PostSerializer, ListFollowerSerializer
from blog.services import feed_service


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

    def get_queryset(self):
        return Post.objects.filter(
            user_id=self.kwargs.get('pk')).select_related('user'[:500])


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





class ListFollowerView(generics.ListAPIView):
    """
    Get user's list of followers
    """
    permission_classes = [IsAuthenticated]
    serializer_class = ListFollowerSerializer

    def get_queryset(self):
        return Follower.objects.filter(user=self.request.user)


class FollowerView(APIView):
    """
    Follow to somebody
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            user = User.objects.get(id=pk)
        except Follower.DoesNotExist:
            return response.Response(status=404)
        Follower.objects.create(subscriber=request.user, user=user)
        return response.Response(status=201)

    def delete(self, request, pk):
        try:
            sub = Follower.objects.get(subscriber=request.user, user_id=pk)
        except Follower.DoesNotExist:
            return response.Response(status=404)
        sub.delete()
        return response.Response(status=204)


class FeedView(GenericViewSet):
    """
    News timeline
    """
    permission_classes = [IsAuthenticated]
    serializer_class = ListPostSerializer

    def list(self, request, *args, **kwargs):
        queryset = feed_service.get_post_list(request.user)
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = feed_service.get_single_post(kwargs.get('pk'))
        serializer = PostSerializer(instance)
        return response.Response(serializer.data)


