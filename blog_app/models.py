from django.db import models
from django.contrib.auth.models import User

class BlogModel(models.Model) : 
    
    title = models.CharField(max_length=70 , blank=True)
    image = models.ImageField(upload_to='uploads/' , blank=True)
    content = models.TextField(max_length=3000 , blank = True)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=30 , blank=True)

    class Meta : 
        ordering = ['timestamp']

class ContactModel(models.Model) :
    name = models.CharField(max_length=50, blank=False)
    phone_no = models.CharField(max_length=15, blank=True , null=True)
    # sender = models.ForeignKey(User , on_delete=models.CASCADE)
    email = models.EmailField(blank=True) # Blank = True for testing purpose
    issue_description = models.TextField(blank=True, null=True)