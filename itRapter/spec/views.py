from __future__ import unicode_literals

from django.shortcuts import render


def show_admin_custom_page(request):
    # some code
    ctx = {'data': 'test'}
    return render(request, 'admin_custom_page.html', ctx)