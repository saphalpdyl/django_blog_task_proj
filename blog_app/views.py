from audioop import reverse
from os import name
from django.shortcuts import render , redirect
from django.http import HttpRequest

from blog_app.models import BlogModel , ContactModel

# Create your views here.

# Blog Show Page
def blog_view(request : HttpRequest) : 
    blog_queryset = BlogModel.objects.all()
    
    return render(request , 'blog_app/blog.html' , {
        'blogs' : blog_queryset,
    })

def about_view(request : HttpRequest) : 
    return render(request , 'blog_app/about.html')

def blog_post_view(request : HttpRequest) : 
    return render(request , 'blog_app/blog_post.html')

def home_view(request : HttpRequest) : 
    return render(request , 'blog_app/home.html')

def contact_view(request : HttpRequest) : 
    
    if request.method == 'POST' : 
        p_name = request.POST['name']
        p_phone_no = request.POST['phone_no']
        p_email = request.POST['email']
        p_issue_description = request.POST['issue_description']
        
        contact_item = ContactModel(name=p_name ,
                                    phone_no=p_phone_no ,
                                   email=p_email ,
                                  issue_description=p_issue_description)
        contact_item.save()
        redirect('home')

    return render(request , 'blog_app/contact.html')