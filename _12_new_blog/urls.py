"""
_12_new_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Uncomment next two lines to enable admin:
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blog_app.views import about_view, blog_post_view, blog_view, contact_view, home_view, login_view , logout_view , register_view, show_issues_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/' , blog_view , name='blog'),
    path('about/' , about_view , name='about'),
    path('blogpost/' , blog_post_view , name='blog_post'),
    path('' , home_view , name='home'),
    path('contact/' , contact_view , name='contact'),
    path('login/' , login_view , name='login'),
    path('logout/' , logout_view , name='logout'),
    path('register/', register_view, name='register'),
    path('show_issues/', show_issues_view, name='show_issues')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)