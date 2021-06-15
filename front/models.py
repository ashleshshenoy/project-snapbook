from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=100)
    image = models.ImageField(default="default.jpg", upload_to='post_pics')
    date_posted = models.DateTimeField(auto_now_add=True)
    location = models.TextField(default="no location")
    like = models.ManyToManyField(User, related_name='post_like')

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return 'Post {} from {}'.format(self.id, self.user.username)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)

    def __str__(self):
        return f'Commented on {self.post.user} post by {self.user}'

    def get_absolute_url(self, **kwargs):
        return reverse('post-detail', kwargs={'pk': self.post.id})
