from django.db import models

# Create your models here.


class cation(models.Model):
    cname = models.CharField(max_length=30)
    def __str__(self):
        return self.cname


class tag(models.Model):
    tagname = models.CharField(max_length=30)
    def __str__(self):
        return self.tagname


class comment(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    website = models.CharField(max_length=30)
    content = models.CharField(max_length=30)
    contenttime = models.DateTimeField(auto_now_add=True)
    artid = models.ForeignKey('article',models.CASCADE)
    def __str__(self):
        return self.username


class article(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    time_creation = models.DateTimeField(auto_now_add=True)
    time_modification = models.DateTimeField(auto_now_add=True)
    number = models.IntegerField(default=0)
    text = models.TextField()
    acation = models.ForeignKey('cation',models.CASCADE)
    atag = models.ManyToManyField(to='tag')
    def __str__(self):
        return self.title