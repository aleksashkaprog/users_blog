from django.contrib.auth.models import User
from django.urls import path
from drf_yasg import openapi

from . import views
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.urlpatterns import format_suffix_patterns


schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='v1',
        description="Описание проекта",
        terms_of_services="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="alexandrsgrusina@gmail.com"),
        license=openapi.License(name='')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),

)

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('posts/', views.PostView.as_view({'post': 'create'}), name='post-create'),
    path('posts/<int:pk>', views.PostView.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    }), name='post-rud'),
    path('posts/<int:pk>', views.PostListView.as_view(), name='post-list'),
    path('followers/<int:pk>', views.FollowerView.as_view(), name='follow'),
    path('followers/list', views.ListFollowerView.as_view(), name='follower-list'),
    path('feed/<int:pk>', views.FeedView.as_view({'get': 'retrieve'}), name='feed'),
    path('feed/timeline', views.FeedView.as_view({'get': 'list'}), name='feed-timeline'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)