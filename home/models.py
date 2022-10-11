from email.policy import default
from django.db import models

# Create your models here.
class Cources(models.Model):

    cid =   models.IntegerField(max_length=1000,default=110110)
    title = models.CharField(max_length=50)
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    auther = models.CharField(max_length=50)
    cname = models.CharField(max_length=50,default='')
    thumb = models.ImageField(upload_to='cources/',default='')

    def __str__(self):
        return self.title