from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class UserProfile(models.Model):
    uid = models.AutoField(primary_key=True,verbose_name='帳號序號',default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='帳號名稱')
    real_name = models.CharField(max_length=30,blank=True, verbose_name='真實姓名')
    gender = models.IntegerField(blank=True, verbose_name='姓別',default=0)# 0 is male , 1 is female
    birthday = models.DateField(blank=True,verbose_name="生日",default=timezone.now)

    def __str__(self):
        return str(self.uid) +" , "+str(self.user)