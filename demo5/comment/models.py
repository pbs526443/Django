from django.db import models
from blog.models import article
# Create your models here.

class Comments(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(blank=True,null=True)
    website = models.URLField(blank=True,null=True)
    content = models.TextField()
    contenttime = models.DateTimeField(auto_now_add=True)
    artid = models.ForeignKey(article,models.CASCADE)
    def __str__(self):
        return self.username