from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Users(User):
    college = models.CharField(max_length=20)
    num = models.CharField(max_length=20)


class Books(models.Model):
    book_name = models.CharField(max_length=20,null=False)
    author = models.CharField(max_length=20,null=False)
    publish_com = models.CharField(max_length=20,null=False)
    publish_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.book_name

class Histroys(models.Model):
    book_id = models.ForeignKey('Books',on_delete=models.CASCADE)
    user_id = models.ForeignKey('Users',on_delete=models.CASCADE)
    user_name = models.CharField(max_length=20,null=False)
    date_borrow = models.DateTimeField(auto_now_add=True)
    date_return = models.DateTimeField()
    status = models.CharField(max_length=20,default='not return')

