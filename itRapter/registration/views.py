from django.core.mail import send_mail
from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.conf import settings

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        context = {'form': form,
                   'username': username,
                   'password1': password1,
                   'password2': password2,
                   'email': email}

        if form.is_valid():
            form.save()
            send_mail('От ItRaptor', 'Мы блогодарим вас за использования в качестве получения основной it информации наш сайт. Мы публикуем статья ежедневно', settings.EMAIL_HOST_USER, [email])
            return redirect('/loginNow/')

    else:
        form = RegisterForm()
        context = {'form': form
                   }

    return render(request, 'registration/LoginNow.html', context)

def indexs(request):
    return render(request, 'ShapeHTML/MainShape.html')

def LoginNow(request):
    return render(request, 'registration/LoginNow.html')

def logout(request):
    return render(request, 'registration/login.html')

def login(request):
    return render(request, 'registration/login.html')

