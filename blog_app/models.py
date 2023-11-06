from django.db import models
from django.contrib.auth.models import User

class BlogModel(models.Model) : 
    
    title = models.CharField(max_length=70 , blank=True)
    image = models.ImageField(upload_to='uploads/' , blank=True)
    content = models.TextField(max_length=3000 , blank = True)
    author = models.CharField(max_length=40 , blank=False , null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=30 , blank=True)

class ContactModel(models.Model) :
    
    name = models.CharField(max_length=50, blank=False)
    phone_no = models.IntegerField(blank=True , null=True)
    email = models.EmailField(blank=True) # Blank = True for testing purpose
    issue_description = models.TextField(blank=True, null=True)