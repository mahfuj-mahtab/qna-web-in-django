from django.db import models
from home.models import *
# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(OurUser, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(OurUser, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)