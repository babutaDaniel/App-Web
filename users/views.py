from django.shortcuts import render, Http404, reverse, redirect
from django.contrib.auth import authenticate, login,logout
from users.forms import RegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from datetime import datetime


def login_user(request):
    if request.user.is_authenticated:
        redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is None:

            raise Http404('Username or password not ok! Go back and type a valid user!')
        else:
            login(request, user)
            return redirect('/')

    return render(request, 'users/login.html', {})


def logout_users(request):
    logout(request)
    return redirect('/')


def register_user(request):
    if request.method == 'GET':
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            Profile.objects.create(user_id=user.id,)
            return redirect('/')

    return render(request, 'users/register.html',{
        'form': form,
    })


@login_required
def show_profile(request):

    if request.method == 'GET':
        form = ProfileForm()
    else:
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

    if form.is_valid():
        form.save()

        return redirect(reverse('users:profile'))

    return render(request, 'users/profile.html', {
            'form': form
         })






