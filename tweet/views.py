from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TweetModel

# Create your views here.

def home(request):
    ur_user = request.user.is_authenticated
    if ur_user:
        return redirect('/tweet')
    else:
        return redirect('/sign-in')

def tweet(request):
    ur_user = request.user.is_authenticated
    if request.method == 'GET':
        if ur_user:
            all_tweet = TweetModel.objects.all().order_by('-created_at')
            return render(request, 'tweet/home.html', {'tweet': all_tweet})
        else:
            return redirect('/sign-in')
    elif request.method == 'POST':
        user = request.user
        my_tweet = TweetModel()
        my_tweet.author = user
        my_tweet.content = request.POST.get('my-content','')#여기서 my-content는 html에서 불러오는 것
        my_tweet.save()
        return redirect('/')

@login_required
def delete_tweet(request,id):
    my_tweet = TweetModel.objects.get(id=id)
    my_tweet.delete()
    return redirect('/tweet')



