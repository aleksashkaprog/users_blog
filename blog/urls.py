from django.contrib.auth.models import User
from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('post', views.PostView.as_view({'post': 'create'})),
    path('post/<int:pk>', views.PostView.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    })),
    path('<int:pk>', views.PostListView.as_view()),
    ]