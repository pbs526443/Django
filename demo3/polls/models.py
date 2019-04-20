from django.db import models

# Create your models here.

class GoodsManage(models.Manager):
    def create_good(self,_name,_age):
        goods = self.model()
        goods.name = _name
        goods.age = _age
        return goods
    def create_goods(self,_name,_age):
        goods = self.create(name=_name,age=_age)
        return goods

class Goods(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    dgmanager = models.Manager()
    dgmanager1 = GoodsManage()

    @classmethod
    def create(cls,_name,_age):
        goods = cls(name=_name,age = _age)
        return goods

    class Meta():
        db_table = 'goods'
        ordering = ['age','-name']





# 一对
class temp(models.Model):
    name = models.CharField(max_length=20)
# 一
class temp2(models.Model):
    fname = models.CharField(max_length=20)
    uid = models.OneToOneField('temp',on_delete=models.CASCADE)
# 多对
class Host(models.Model):
    hostname = models.CharField(max_length=20)
    ip = models.GenericIPAddressField(protocol='ipv4')
    port = models.IntegerField()
# 多
class Application(models.Model):
    name = models.CharField(max_length=20)
    h = models.ManyToManyField('Host')


class vote(models.Model):
    votename = models.CharField(max_length=50)
    def __str__(self):
        return self.votename

class option(models.Model):
    options = models.CharField(max_length=20)
    number = models.IntegerField(default=0)
    voteid = models.ForeignKey('vote',on_delete=models.CASCADE)

    def __str__(self):
        return self.options