#user/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
#장고가 관리하는 설정에서 setting을 불러오는 것.


# Create your models here.
class UserModel(AbstractUser):
    class Meta: #데이터베이스에 정보를 넣어주는 역할
        db_table = "my_user"#내 db테이블이 my_user였으면 좋겠다

    bio = models.CharField(max_length=256, default='')
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followee')#우리 user모델을 m-to-m필드로 불러오고 싶다.



