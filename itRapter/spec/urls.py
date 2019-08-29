from django.conf.urls import url
from django.contrib.auth.decorators import user_passes_test
from django.urls import path

from spec.views import show_admin_custom_page

urlpatterns = [
    path('admin-custom-page/', user_passes_test(lambda u: u.is_superuser)(show_admin_custom_page), name='show_admin_custom_page'),
]