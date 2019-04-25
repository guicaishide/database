from django.db import models
from django.contrib.auth.models import  AbstractUser

class Myuser(AbstractUser):
    mobile =models.CharField(max_length=11,verbose_name='手机',default='')

    class Meta:
        #起名为用户信息
        verbose_name='用户信息'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.username