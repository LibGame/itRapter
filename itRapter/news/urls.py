"""RapterGames URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.template.context_processors import static
from django.urls import path, include
from django.views.generic import ListView, DetailView
from django.conf.urls.static import static
from django.conf import settings

from .views import ArticleIndex
from .import views

urlpatterns=[
    path('', ArticleIndex.as_view(), name='articles_list'),
    path('news/<slug:slug>/', views.ArticleDetailView, name='article_detail'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('tag/<tag_slug>.+/', views.post_list, name='post_list_by_tag'),
    path('tag/<tag_slug>.+/', views.tags_list, name='post_tags_by_tag'),
    path('<slug:slug>/like', views.addlike, name='pk'),
    path('<slug:slug>/dislike', views.adddislike, name='pk'),
    path('search/', views.post_search, name='post_search'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
