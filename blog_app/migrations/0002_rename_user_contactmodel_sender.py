# Generated by Django 4.1 on 2023-11-12 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactmodel',
            old_name='user',
            new_name='sender',
        ),
    ]
