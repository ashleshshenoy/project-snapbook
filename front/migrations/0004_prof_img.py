# Generated by Django 3.2 on 2021-05-07 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0003_auto_20210507_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='prof',
            name='img',
            field=models.ImageField(default='media/default.jpg', upload_to=''),
        ),
    ]
