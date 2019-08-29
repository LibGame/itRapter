"""itRapter URL Configuration

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
from django.urls import path, include
from django.conf.urls.static import static

from itRapter import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('', include('news.urls')),
    path('', include('registration.urls')),
    path('', include('comment.urls')),
    path('', include('spec.urls')),
    path('', include('cabinet.urls')),
    path('', include('MainPage.urls')),
    path('programms/', include('programs.urls')),
    path('lessons_java/', include('lessons_java.urls')),
    path('lessons_django/', include('lessons_django.urls')),
    path('lessons_c/', include('lessons_c.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls'))

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
