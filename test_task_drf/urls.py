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
    GroupAPIList, GroupAPICreate, GroupAPIUpdate, GroupAPIDelete,
    UserAPICreate, UserAPIDelete, UserAPIList, UserAPIUpdate)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/all_users', UserAPIList.as_view()),
    path('api/v1/add_new_user', UserAPICreate.as_view()),
    path('api/v1/update_user/<int:pk>/', UserAPIUpdate.as_view()),
    path('api/v1/delete_user/<int:pk>/', UserAPIDelete.as_view()),
    path('api/v1/group_list', GroupAPIList.as_view()),
    path('api/v1/add_new_group', GroupAPICreate.as_view()),
    path('api/v1/update_group/<int:pk>/', GroupAPIUpdate.as_view()),
    path('api/v1/delete_group/<int:pk>/', GroupAPIDelete.as_view()),
]
