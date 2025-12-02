from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import CASCADE

# Create your models here.

#Blogger (Blog Author) model
class Blogger(models.Model):
    author = models.OneToOneField(User, on_delete=CASCADE)
    bio = models.TextField(max_length=500, help_text="Tell us about yourself!")

    def get_absolute_url(self):
        return reverse('blogger-detail', args=[str(self.id)])

    def __str__(self):
        return self.user.username
    
#BlogPost model    
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Blogger, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])
    
class Comment(models.Model):
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

