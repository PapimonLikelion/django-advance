from django.db import models
from django.conf import settings

# Create your models here.
class UserPost(models.Model):
    title = models.CharField(max_length=100)    
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)


# createsuperuser로 author 2명을 만들기로하자
# 1번 유저
# 2번 유저