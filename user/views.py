from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def sign_up_view(request):
    if request.method=='POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        bio = request.POST.get('bio', None)

        exist_user = get_user_model().objects.filter(username=username)
        if password != password:
            return render(request, 'user/signup.html')
        elif exist_user:
            return render(request, 'user/signup.html')
        else:
            UserModel.objects.create_user(username=username,password=password, bio=bio)
            return redirect('/sign-in')

    elif request.method == 'GET':
        ur_user = request.user.is_authenticated
        if ur_user:
            return redirect('/')
        else:
            return render(request, 'user/signup.html')


def sign_in_view(request):

    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('/tweet')
        else:
            return redirect('/sign-in')
    elif request.method == 'GET':
        ur_user = request.user.is_authenticated
        if ur_user:
            return redirect('/')
        else:
            return render(request, 'user/signin.html')

@login_required()
def logout(request):
    auth.logout(request)
    return redirect('/')