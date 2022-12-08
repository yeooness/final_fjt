

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('grade', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dogwalking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('members', models.IntegerField(default=1, null=True)),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('like_user', models.ManyToManyField(blank=True, related_name='like_dogwalking', to=settings.AUTH_USER_MODEL)),
                ('pet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pet', to='accounts.pet')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('dogwalking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dogwalking.dogwalking')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('read', models.BooleanField(default=False)),
                ('important', models.BooleanField(default=False)),
                ('garbage', models.BooleanField(default=False)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_from_dw', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_to_dw', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
