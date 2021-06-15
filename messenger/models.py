from django.db import models
from django.utils import tree
from django.contrib.auth.models import User

class Message(models.Model):
    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name='msg_sent_list')
    receiver=models.ForeignKey(User,on_delete=models.CASCADE, related_name='msg_received_list')
    message=models.TextField(blank=False)
    date=models.DateTimeField(auto_now=True)    
    unread=models.BooleanField(default=True,blank=True)
