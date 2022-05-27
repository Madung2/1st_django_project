from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect("/tweet")
    else:
        return redirect("/sign-in")

def tweet(request):
    if request.method =='GET':
        user = request.user.is_authenticated #로그인 인증한 유저를 찾음
        if user: #로그인한 사람이 있다면
            return render(request, 'tweet/home.html')
        else:
            return redirect("/sign-in")