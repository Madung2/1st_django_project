from django.urls import path
from . import views


#네임은 다른데서 불러서 사용할 수 있는 이름.
urlpatterns = [
    path('', views.home, name='home'),# 127.0.0.1:8000 과 views.py 폴더의 home 함수 연결
    path('tweet/', views.tweet, name='tweet'),# 127.0.0.1:8000/tweet 과 views.py 폴더의 tweet 함수 연결
    path('tweet/<int:id>', views.detail_tweet, name='detail-tweet'),
    path('tweet/delete/<int:id>', views.delete_tweet, name='delete-tweet'), #숫자가 올건데 id라는 변수에 저장하겠다
    path('tweet/comment/<int:id>', views.write_comment, name='write-comment'),
    path('tweet/comment/delete/<int:id>', views.delete_comment, name='delete-comment'),
]