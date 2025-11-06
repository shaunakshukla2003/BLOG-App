from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid
# Create your models here.
class Contact(models.Model):
    sn=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=100)
    number=models.CharField(max_length=13)
    
    issue=models.TextField()
    def __str__(self):
        return "Message from" " "+ self.name + " - " + self.email
    
class Post(models.Model):
    sn=models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='blog_images/',blank=True,null=True)
    title=models.CharField(max_length=255)
    content=models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100,unique=True,blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            mod_slug = f"{self.title}-{uuid.uuid4()}"
            self.slug = slugify(mod_slug)
        super().save(*args,**kwargs)
    
    def __str__(self):
        return f"{self.title} by {self.author.username}"
    