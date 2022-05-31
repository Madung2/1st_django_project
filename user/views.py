from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib.auth import get_user_model

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
            new_user = UserModel()
            new_user.username = username
            new_user.password = password
            new_user.bio = bio
            new_user.save()
        return redirect('/sign-in')

    elif request.method == 'GET':
        return render(request, 'user/signup.html')


def sign_in_view(request):
    if request.method == 'POST':
        return HttpResponse("로그인 성공")
    elif request.method == 'GET':

        return render(request, 'user/signin.html')