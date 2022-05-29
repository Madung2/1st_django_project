from django.shortcuts import render, redirect

# Create your views here.

#유저가 확인하면 tweet으로 redirect 보내는 함수?!
def home(request):
    ur_user = request.user.is_authenticated
    if ur_user:
        return redirect('/tweet')
    else:
        return redirect('/sign-in')

#redirect된 상태에서 GET으로 화면 불러오는 함수
def tweet(request):
    if request.method == 'GET':
        ur_user = request.user.is_authenticated
        if ur_user:
            return render(request, 'tweet/home.html')
        else:
            return redirect('/sign-in')
