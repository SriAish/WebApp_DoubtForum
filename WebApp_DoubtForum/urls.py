"""WebApp_DoubtForum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from DoubtForum.views import *
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('add_doubt/',add_doubt,name='add_doubt'),
    path('tag_list/',tag_list,name='tag_list'),
    path('<int:pk>/',doubt_complete,name='doubt_complete'),
    path('<tag>/',tagged_doubts,name='tagged_doubts'),
]
