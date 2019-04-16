from django.db import models

# Create your models here.

'''
django MVT M
ORM 对象中的O
需要定义实体类


定义模型：继承models.Model

python manage.py makemigrations 生成迁移文件
python manage.py migrate 执行迁移
'''

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(auto_now_add=True)

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=50)
    # 外键 第一个参数为表名  第二个参数代表删除类型
    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE)