from django.db import models
from django.contrib.auth.models import User
#회원가입 할 수 있는 모델 제작
#null=True는 많이 쓰지 않는 것이 좋음

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, unique=True)
  nickname = models.CharField(max_length=10, null=True, unique=True)
  image = models.ImageField(upload_to='profile/', null=True)

  class Meta:
    db_table = 'profile'
  
  def __str__(self):
    return self.nickname