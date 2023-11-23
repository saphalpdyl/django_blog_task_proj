from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE
from django_quill.fields import QuillField

from blog_app.models import BlogModel, ContactModel

@admin.register(ContactModel)
class ContactModelView(admin.ModelAdmin) :
    list_display = ['id' , 'name' , 'email' , 'phone_no' , 'issue_description']

@admin.register(BlogModel)
class ContentView(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'author' , 'content' , 'image' , 'timestamp' , 'slug']
    
    formfield_overrides = {
        
        models.TextField: {'widget': TinyMCE(
            attrs={'cols': 80, 'rows': 30},
            mce_attrs={
                'plugins': 'advlist autolink lists link image charmap print preview hr anchor pagebreak',
                'toolbar': 'undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image | charmap | preview',
                'image_advtab': True,
                'media_alt_source': True,
                'content_css': '/static/css/custom-tinymce.css',
                'file_picker_types': 'file image media',
                'file_picker_callback': 'function(callback, value, meta) { tinymce.activeEditor.windowManager.open({ title: "File Manager", file: "/file-manager/tinymce5", width: 800, height: 600, resizable: "yes", close_previous: "no", onMessage: function(api, message) { callback(message.content); } }); }'
            }
        )}
    }

# Register your models here.
# admin.site.register(ContactModel , ContactModelView)
# admin.site.register(BlogModel, ContentView)