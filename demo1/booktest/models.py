from django.db import models

# Create your models here.

'''
django MVT M
ORM 对象中的O
需要定义实体类


定义模型：继承models.Model
配置数据库：默认sqlite
将应用名添加到应用列表settings.py文件里

python manage.py makemigrations 生成迁移文件
python manage.py migrate 执行迁移

'''

'''
python manage.py shell 进入命令：不需要运行项目就可以操作数据库

导入类 from booktest.models import HeroInfo,BookInfo
查找所有行  表名.objects.all()
根据主键查找 表名.objects.get(pk=1)
添加对象 **.save()
修改对象  **.save()
删除对象 **delete()

如果存在一对多关系： 一方.多方类名小写_set.all() 可以查询一对多关系

一对多:  一方村子主键   多方存在主键和外键（一方中的主键）

类名.objects.create(列名=值)
'''

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.btitle

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=50)
    # 外键 第一个参数为表名  第二个参数代表删除类型
    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE)
    def __str__(self):
        return self.hname