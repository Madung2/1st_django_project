from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model #사용자가 데이터베이스 안에 있는지 검사하는 함수
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
'''
1.GET인지 POST인지 확인한다.
2.POST라면 먼저 post리퀘스트르 받고
3. 패스워드 1과 2가 같은지 확인
4. 같은 유저가 db에 있는지 확인
5. 없다면 sign-in으로 redirect
6. GET이라면 is_authenticated 하기
'''

def sign_up_view(request):
    if request.method == 'GET':
        ur_user = request.user.is_authenticated
        if ur_user:
            return redirect('/')
        else:
            return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        bio = request.POST.get('bio', None)

        if password != password2:
            return render(request, 'user/signin.html')
        else:
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html')
            else:
                UserModel.objects.create_user(username=username, password=password, bio=bio)
                return redirect('/sign-in')


def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None) #html의 input->name과 동일하게 작성
        password = request.POST.get('password', None)

        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return redirect('/sign-in')
    elif request.method == 'GET':
        ur_user = request.user.is_authenticated
        if ur_user:
            return redirect('/')
        else:
            return render(request, 'user/signin.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')
    #로그인이 되어 있다면 tweet으로 보내주고 로그아웃이 되어 있다면 로그인 페이지로 보내줄거임