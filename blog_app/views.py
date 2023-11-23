from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.paginator import Paginator

from blog_app.models import BlogModel, ContactModel

# Blog Show Page
@login_required(login_url='/')
def blog_view(request: HttpRequest):
    blog_queryset = BlogModel.objects.all()

    paginator = Paginator(blog_queryset , 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    total_pages = paginator.num_pages

    return render(request, 'blog_app/blog.html', {
        'blogs': blog_queryset,
        'page_obj' : page_obj,
        'total_pages' : total_pages,
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

        user = authenticate(request, username=username , password=password)

        if user : 
            login(request, user)
            messages.success(request, "Succesfully logged in ")
            return redirect(reverse_lazy('blog'))
        else : 
            messages.error(request, "Invalid Credentials")
            return redirect(reverse_lazy('home'))
    else : 
        return redirect(reverse_lazy('home'))
    
def logout_view(request: HttpRequest) :
    if request.method == "GET" :
        if request.user.is_authenticated : 
            logout(request)
            return redirect(reverse_lazy('blog'))
    
    return redirect(reverse_lazy('home'))

def register_view(request: HttpRequest) :

    if request.method == "POST" : 
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        # Check for existing email
        if User.objects.filter(email=email).exists() : 
            messages.error(request, "User already exists")
            return redirect(reverse_lazy('home'))
        
        # Register the user
        User.objects.create_user(username=first_name, first_name=first_name, last_name=last_name, email=email, password=password)
        return redirect(reverse_lazy('home'))
        
    
    return render(request, 'blog_app/register.html')

@login_required(login_url='/')
@staff_member_required
def show_issues_view(request: HttpRequest) : 

    contact_queryset = ContactModel.objects.all()

    return render(request, 'blog_app/show_issues.html' , {
        'issues' : contact_queryset
    })

def search(request: HttpRequest) : 
    query = request.GET['query']
    if len(query) == 0 : 
        messages.error(request , "No query!")
        all_post = {}
    else :
        if len(query) > 78 : 
            all_post= BlogModel.objects.none()
        else:
            all_post_title = BlogModel.objects.filter(title__icontains=query)
            all_post_content = BlogModel.objects.filter(content__icontains=query)
            all_post = all_post_title.union(all_post_content)
            # all_post = (all_post_content | all_post_title).distinct() # This works too 

        if all_post.count() == 0 :
            messages.warning(request, "No search results found")

    return render(request, 'blog_app/search.html' , {
        'all_post' : all_post,
        'query' : query
    })