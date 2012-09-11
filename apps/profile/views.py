from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout

from profile.forms import LoginForm


def user_login(request):
    """
    The default login page
    """
    
    template = 'profile/login.html'
    context = {
        'breadcrumbs': ['Login', ],
        'form': None
    }

    if request.method == 'POST':
        context['form'] = LoginForm(request.POST)
        if context['form'].is_valid():
            login(request, context['form'].user)
            template = 'profile/login_success.html'
    else:
        context['form'] = LoginForm()

    return render(request, template, context)


def user_logout(request):
    """
    The default login page
    """
    
    template = 'profile/login.html'
    context = {
        'breadcrumbs': ['Login', ],
        'form': None
    }

    logout(request)

    return redirect('/')
