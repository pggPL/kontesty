from django.shortcuts import render, HttpResponse, redirect
from app.login import *
from app.main import *
from django.http import FileResponse, Http404


# Create your views here.

def index(request):
    context = set_context(request)
    return render(request, "app/index.html", context)


def user_panel(request):
    context = set_context(request)
    return render(request, 'app/userpanel.html', context)


def register(request):
    context = set_context(request)
    # Teraz obsługujemy żądzanie rejestracji
    reg_state = Account.try_register(request)
    if reg_state == "OK":
        return redirect('user_panel')
    if reg_state == "Username used":
        context['username_used'] = True
        return render(request, 'app/register.html', context)
    return render(request, 'app/register.html', context)


def rules(request):
    context = set_context(request)
    return render(request, 'app/rules.html', context)


def user_settings(request):
    print(Account.try_change_data(request))
    context = set_context(request)
    if Account.try_change_data(request) is True:
        context['changed'] = True

    return render(request, 'app/user_settings.html', context)


def login(request):
    context = set_context(request)
    reg_state = Account.try_login(request)
    if reg_state == "OK":
        return redirect('user_panel')
    if reg_state == "Username used":
        context['username'] = True
        context['wrong_password'] = True
        return render(request, 'app/index.html', context)
    if reg_state == "Wrong password":
        context['wrong_password'] = True
        return render(request, 'app/index.html', context)
    return render(request, 'app/userpanel.html', context)


def logout(request):
    Account.logout(request);
    context = set_context(request)
    return render(request, "app/index.html", context)


def change_password(request):
    context = set_context(request)
    if Account.try_change_password(request) is True:
        context['changed']=True
    if not context['logged']:
        redirect('index')
    return render(request, 'app/change_password.html', context)


def problems(request):
    context = set_context(request)
    if context['contest_in_progress']:
        return FileResponse(open('app/problems/problems.pdf', 'rb'), content_type='application/pdf')
    else:
        redirect('index')
