# Generated by Django 3.2 on 2021-05-16 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0011_remove_post_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='about',
            new_name='caption',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='img',
            new_name='image',
        ),
    ]
