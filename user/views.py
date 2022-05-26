from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse

# Create your views here.
def sign_up_view(request):
    #1.먼저 GET인지 POST인지 확인하는 if 문
    if request.method == 'GET':
        return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        #유저네임을 post로 리퀘스트 받겠다. 유저네임이 없으면 None=빈칸으로 처리하겠다
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        bio = request.POST.get('bio', None)
        #2. 패스워드 2개가 다른지 같은지

        if password != password2:
            return render(request, 'user/signin.html')
        else:
            new_user = UserModel()
            new_user.username = username
            new_user.password = password
            new_user.bio = bio
            new_user.save()
        return redirect('/sign-in')


def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None) #html의 input->name과 동일하게 작성
        password = request.POST.get('password', None)

        me = UserModel.objects.get(username=username)
        if me.password == password:
            request.session['user'] = me.username
            return HttpResponse("로그인 성공!")
        else:
            return redirect('/sign-in')
    elif request.method == 'GET':
        return render(request, 'user/signin.html')