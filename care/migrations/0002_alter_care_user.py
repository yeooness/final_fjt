# Generated by Django 3.2.13 on 2022-12-08 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('care', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='care',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='care', to=settings.AUTH_USER_MODEL),
        ),
    ]
