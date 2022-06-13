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
from django.urls import include, path, re_path

from network_users.views import GroupViewSet, MembersViewSet, UserViewSet
from test_task_drf.router import UserGroupRouter


router = UserGroupRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'group', GroupViewSet, basename='group')

urlpatterns = [
    path('admin', admin.site.urls),
    path('api/v1/', include(router.urls)),
    re_path('^api/v1/group/(?P<group_pk>\d+)/users/?$', MembersViewSet.as_view({'get': 'list', 'post': 'create'})),
    re_path('^api/v1/group/(?P<group_pk>\d+)/users/(?P<user_pk>\d+)/?$',
            MembersViewSet.as_view({'get': 'list', 'delete': 'destroy'})),
]
