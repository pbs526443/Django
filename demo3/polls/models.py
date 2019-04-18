from django.db import models

# Create your models here.


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