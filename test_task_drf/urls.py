"""test_task_drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from network_users.views import (
    GroupViewSet, UsersInGroupViewSet, UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user/', UserViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/user/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('api/v1/group/', GroupViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/group/<int:pk>/', GroupViewSet.as_view({'put': 'partial_update', 'delete': 'destroy'})),
    path('api/v1/group/<int:group_pk>/users/', UsersInGroupViewSet.as_view({'get': 'list', 'post': 'update'})),
    path('api/v1/group/<int:group_pk>/users/<int:user_pk>',
         UsersInGroupViewSet.as_view({'get': 'list', 'delete': 'destroy'})),
    #  path('api/v1/user', GET - get all users, POST - add user,
    #  path('api/v1/user/{id}' - PUT - update, PATCH - partial update, DELETE - delete user
    #  path('api/v1/group/<int:pk>/users', # GET - list users in group, POST - add user, DELETE - remove user
    #  AddUserToGroup.as_view()),
]
