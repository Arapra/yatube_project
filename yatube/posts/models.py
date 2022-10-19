from statistics import mode
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model() 

class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    group = models.ForeignKey('Group', on_delete=models.CASCADE, blank=True, null=True, )

class Group(models.Model):
    title = models.TextField()
    slug = models.SlugField()
    description = models.TextField()
    
    def __str__(self) -> str:
        return self.title