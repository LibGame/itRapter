from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns =[
    path('register/', views.register, name='register'),
    path(r'login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path(r'logout/', LogoutView.as_view(next_page='registration/login.html'), name='logout'),
    path('accounts/profile/', views.indexs, name='indexs'),
    path('loginNow/', views.LoginNow, name='LoginNow'),
    path('logout/registration/login.html', views.indexs, name='indexs')
]
