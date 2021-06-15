from django.db import models
from django.contrib.auth.models import User
from django.db.models.enums import Choices
# Create your models here.

class Notification(models.Model):
    notify_to=models.ForeignKey(User,on_delete=models.CASCADE,related_name='notifed_to')
    notify_from=models.ForeignKey(User,on_delete=models.CASCADE,related_name='notified_by')
    choice=(
        ('admin','admin'),
        ('comment','comment'),
        ('like','like')
    )
    notify_type=models.CharField(choices=choice,max_length=20)
    notify_msg=models.CharField(max_length=100,blank=True)