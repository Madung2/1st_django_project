#user/models.py
from django.db import models


# Create your models here.
class UserModel(models.Model):
    class Meta: #데이터베이스에 정보를 넣어주는 역할
        db_table = "my_user"#내 db테이블이 my_user였으면 좋겠다

    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=256, null=False)
    bio = models.CharField(max_length=256, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #CharField :어떤 형태로 데이터베이스에 들어갈것인지


