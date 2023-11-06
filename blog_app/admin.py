from django.contrib import admin

from blog_app.models import BlogModel, ContactModel

class BlogModelView(admin.ModelAdmin) : 
    list_display = ['id' , 'title' , 'author' , 'content' , 'image' , 'timestamp' , 'slug']

class ContactModelView(admin.ModelAdmin) :
    list_display = ['id' , 'name' , 'email' , 'phone_no' , 'issue_description']

# Register your models here.
admin.site.register(BlogModel , BlogModelView)
admin.site.register(ContactModel , ContactModelView)