# Generated by Django 3.2.13 on 2022-11-29 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dogwalking', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='Dogwalking',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dogwalking.dogwalking'),
            preserve_default=False,
        ),
    ]
