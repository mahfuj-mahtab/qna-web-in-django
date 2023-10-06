from django.db import models
from home.models import *
from questions.models import *
# Create your models here.
class Answer(models.Model):
    id =models.IntegerField(primary_key =True)
    Q_answer= models.CharField(max_length = 30)
    dislike= models.IntegerField()
    like =models.IntegerField()
    u_email = models.CharField(max_length=100,null=True)
    Q_ID = models.CharField(max_length=100,null=True)