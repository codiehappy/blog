from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name 

class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = RichTextField()
    image = models.ImageField(upload_to='images')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return self.title

