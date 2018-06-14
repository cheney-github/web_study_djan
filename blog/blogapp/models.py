from django.db import models
from django.utils import timezone
# Create your models here.


class Page(models.Model):
    title = models.CharField(max_length=200)
    pic   = models.CharField(max_length=200)
    text  = models.CharField(max_length=200,default="")
    link  = models.CharField(max_length=200,default="")
    update = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Wenzhang(models.Model):
    biaoti = models.CharField(max_length=200,default="")
    zhengwen = models.CharField(max_length=200,default="")

    def __str__(self):
        return self.biaoti
