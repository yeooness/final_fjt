# Generated by Django 3.2.13 on 2022-11-29 02:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_user_blocking'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='liking',
            field=models.ManyToManyField(related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]
