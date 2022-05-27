#user/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserModel(AbstractUser): #모델스.모델의 기능들을 함께 사용하겠다
    class Meta: #데이터베이스에 정보를 넣어주는 역할
        db_table = "my_user"#내 db테이블이 my_user였으면 좋겠다
    bio = models.CharField(max_length=256, default='')
    #CharField :어떤 형태로 데이터베이스에 들어갈것인지



