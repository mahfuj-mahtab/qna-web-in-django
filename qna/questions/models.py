from django.db import models
from home.models import *

# Create your models here.
class Questions(models.Model):
    id =models.IntegerField(primary_key =True)
    title = models.CharField(max_length = 30)
    details = models.CharField(max_length = 50)
    u_email = models.CharField(max_length=50,null = True)
    cat_name = models.CharField(max_length=100,null=True)
    time = models.DateTimeField(auto_now_add=True,null = True)
