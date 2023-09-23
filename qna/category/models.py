from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key = True)
    cat_name = models.CharField(max_length=150)