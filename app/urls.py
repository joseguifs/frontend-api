"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from login import views
from genres.views import GenreView, GenreDetailView, GenreCreateView
from actors.views import ActorView, ActorDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(), name="login_api"),
    path('login/recuperar/',views.RecuperarSenha.as_view(), name = 'recuperar-senha'),
    path('genres/', GenreView.as_view(), name="genres"),
    path('genres/<int:pk>/', GenreDetailView.as_view(), name='genres_detail'),
    path('genres/create/', GenreCreateView.as_view(), name = 'genre_create'),
    path('actors/', ActorView.as_view(), name='actor'),
    path('actors/<int:pk>/',ActorDetailView.as_view(), name = 'actor_detail')
]
