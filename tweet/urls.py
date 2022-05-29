from django.urls import path
from . import views


#네임은 다른데서 불러서 사용할 수 있는 이름.
urlpatterns = [
    path('', views.home, name='home'),# 127.0.0.1:8000 과 views.py 폴더의 home 함수 연결
    path('tweet/', views.tweet, name='tweet')# 127.0.0.1:8000/tweet 과 views.py 폴더의 tweet 함수 연결
]