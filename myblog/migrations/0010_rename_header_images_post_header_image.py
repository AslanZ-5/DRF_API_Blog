# Generated by Django 3.2.7 on 2021-09-18 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0009_rename_header_image_post_header_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='header_images',
            new_name='header_image',
        ),
    ]