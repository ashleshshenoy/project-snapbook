# Generated by Django 3.2 on 2021-05-07 09:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('front', '0004_prof_img'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='prof',
            new_name='post',
        ),
    ]
