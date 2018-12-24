"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from webapp.views import ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView
from accounts.views import login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProjectListView.as_view(), name='project_list'),
    path('projects/<int:pk>', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/create', ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/update', ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/delete', ProjectDeleteView.as_view(), name='project_delete'),
    path('accounts/login', login_view, name='login'),
    path('accounts/logout', logout_view, name='logout'),
]
