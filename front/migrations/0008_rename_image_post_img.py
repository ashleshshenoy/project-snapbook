# Generated by Django 3.2 on 2021-05-12 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0007_rename_img_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='img',
        ),
    ]
