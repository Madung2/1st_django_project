# Generated by Django 3.2.5 on 2022-05-27 22:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='follow',
            field=models.ManyToManyField(related_name='followee', to=settings.AUTH_USER_MODEL),
        ),
    ]
