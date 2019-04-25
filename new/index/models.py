from django.db import models

# Create your models here.
class AccountModel(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="photo")
    number = models.IntegerField()
    news =models.IntegerField()
    new_number=models.IntegerField()
    class Meta:
        db_table='account'

    def __str__(self):
        return self.name

class ArticleModel(models.Model):
    title = models.CharField(max_length=5000)
    pic = models.ImageField(upload_to="pic")
    time = models.DateTimeField()
    read = models.IntegerField()
    looking=models.IntegerField()
    comment = models.IntegerField()
    share = models.IntegerField()
    account=models.ForeignKey(AccountModel,on_delete=models.CASCADE)

    class Meta:
        db_table='article'


class LeftModel(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        db_table='left'

class LeftMiddleModel(models.Model):
    name = models.CharField(max_length=100)
    type= models.CharField(max_length=100)
    class Meta:
        db_table='leftmiddle'