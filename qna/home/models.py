from django.db import models

class OurUser(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 30,null = True)
    email = models.CharField(max_length = 50,null = True)
    password = models.TextField(null = True)
    Bio = models.TextField(null = True)
    Num_of_followers = models.IntegerField(null = True)
    Num_of_following = models.IntegerField(null = True)
    user = models.CharField(max_length = 100,null = True)
    img = models.ImageField(upload_to='images/', null= True)
    phone_No = models.CharField(max_length = 15, null= True)
