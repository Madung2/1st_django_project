# tweet/models.py
from django.db import models
from user.models import UserModel#유저모델을 user.modles에서 가져오겠다.


# Create your models here.
class TweetModel(models.Model):
    class Meta:
        db_table = "tweet"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE) #foreign key= 다른 데이터베이스에서 정보를 가져오겠다
    content = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)