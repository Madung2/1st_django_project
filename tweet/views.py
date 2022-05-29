from django.shortcuts import render, redirect
from .models import TweetModel
from django.contrib.auth.decorators import login_required

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
            all_tweet = TweetModel.objects.all().order_by('-created_at')
            return render(request, 'tweet/home.html', {'tweet': all_tweet}) #요 트윗 키값은 html 템플릿에서 사용됨
        else:
            return redirect('/sign-in')

    elif request.method =='POST':
        user = request.user #로그인된 사용자의 전체 정보
        my_tweet = TweetModel() #이거 왠지 필수...나제?!?! : 클래스는 빵틀이라서
        my_tweet.author = user
        my_tweet.content = request.POST.get('my-content', '') #my-content는 html form name
        my_tweet.save()
        return redirect('/tweet')

@login_required()
def delete_tweet(request, id):
    my_tweet = TweetModel.objects.get(id=id) #url에 id를 넘겨줘야함
    my_tweet.delete()
    return redirect('/tweet')

