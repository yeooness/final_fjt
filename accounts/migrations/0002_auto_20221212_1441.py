# Generated by Django 3.2.13 on 2022-12-12 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='weight',
            field=models.FloatField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pet',
            name='size',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
