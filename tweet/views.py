from django.shortcuts import render, redirect
from .models import TweetModel, TweetComment
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
    my_tweet = TweetModel.objects.get(id=id) #url에 id를 넘겨줘야함 :출처는 모르겠는데 트윗 id인듯 html 트윗 id와 model id가 같을때를 찾아야 할 테니까
    my_tweet.delete()
    return redirect('/tweet')


# @login_required()
# def click_tweet_detail(request, id):
#     # return redirect('/tweet/'+str(id))
#     ur_user = request.user.is_authenticated
#     if ur_user:
#         return redirect('/tweet/'+str(id))
#     else:
#         return redirect('/sign-in')

@login_required()
def detail_tweet(request, id): #요것도 상세트윗의 아이디값을 html에서 받아온는 형태일듯
    my_tweet = TweetModel.objects.get(id=id)  # 상세트윗의 아이디값과 같은 트윗모델을 불러온다
    tweet_comment = TweetComment.objects.filter(tweet_id=id).order_by('-created_at') #트윗코멘의 트윗아이디가 클릭한 id값과 같은것을 불러와서 시간 역순으로 정렬
    return render(request, 'tweet/tweet_detail.html', {'tweet': my_tweet, 'comment': tweet_comment})


@login_required()
def write_comment(request, id):
    if request.method == 'POST':
        comment = request.POST.get("comment", '') #여기서 comment는 아무래도 input의 name에서 오는것 같음
        current_tweet = TweetModel.objects.get(id=id)

        TC = TweetComment()
        TC.comment = comment
        TC.author = request.user
        TC.tweet = current_tweet
        TC.save()

        return redirect('/tweet/'+str(id))

@login_required
def delete_comment(request, id):
    comment = TweetComment.objects.get(id=id)
    current_tweet = comment.tweet.id
    comment.delete()
    return redirect('/tweet/'+str(current_tweet))
