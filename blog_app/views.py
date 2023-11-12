from os import name
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , logout , authenticate
from django.urls import reverse_lazy

from blog_app.models import BlogModel, ContactModel


# Create your views here.

# Blog Show Page
@login_required(login_url='/')
def blog_view(request: HttpRequest):
    blog_queryset = BlogModel.objects.all()

    return render(request, 'blog_app/blog.html', {
        'blogs': blog_queryset,
    })


def about_view(request: HttpRequest):
    return render(request, 'blog_app/about.html')


def blog_post_view(request: HttpRequest):
    return render(request, 'blog_app/blog_post.html')


def home_view(request: HttpRequest):
    return render(request, 'blog_app/home.html')


def contact_view(request: HttpRequest):
    if request.method == 'POST':
        p_name = request.POST['name']
        p_phone_no = request.POST['phone_no']
        p_email = request.POST['email']
        p_issue_description = request.POST['issue_description']

        contact_item = ContactModel(name=p_name,
                                    phone_no=p_phone_no,
                                    email=p_email,
                                    issue_description=p_issue_description)
        contact_item.save()
        redirect('home')

    return render(request, 'blog_app/contact.html')

def login_view(request: HttpRequest) :
    if request.method == "POST" : 
        username = request.POST['username']
        password = request.POST['password']

        print("Somebody Logged in as {}".format(username))

        user = authenticate(request, username=username , password=password)

        if user : 
            login(request, user)
            return redirect(reverse_lazy('blog'))
        else : 
            return redirect(reverse_lazy('home'))
    else : 
        return redirect(reverse_lazy('home'))
    
def logout_view(request: HttpRequest) :
    if request.method == "GET" :
        if request.user.is_authenticated : 
            logout(request)
            return redirect(reverse_lazy('blog'))
    
    return redirect(reverse_lazy('home'))