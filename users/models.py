from django.db import models
from  django.contrib.auth.models import User

from PIL import Image


class Profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    image= models.ImageField(default='default.jpg',upload_to='profile_pics')
    public=models.BooleanField(default=True)
    followers= models.ManyToManyField(User,related_name='followers_list',blank=True)
    following= models.ManyToManyField(User,related_name='following_list',blank=True)
    follow_request=models.ManyToManyField(User,related_name='request_list',blank=True)

    def __str__(self):
        return f'{self.user.username}'

    def save(self,*args,**kwargs):
        super().save(*args, **kwargs)
        img=Image.open(self.image.path)
        if img.height>300 or  img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save
