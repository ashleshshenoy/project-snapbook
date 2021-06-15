# Generated by Django 3.2 on 2021-06-04 01:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0008_auto_20210604_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='follow_request',
            field=models.ManyToManyField(related_name='request_list', to=settings.AUTH_USER_MODEL),
        ),
    ]
