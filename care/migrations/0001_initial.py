

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Care',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='title')),
                ('content', models.TextField(verbose_name='content')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('caring_animal', models.CharField(default='', max_length=300, verbose_name='caring_animal')),
                ('caring_time', models.CharField(max_length=300, verbose_name='caring_time')),
                ('etc', models.CharField(max_length=300, verbose_name='etc')),
                ('area', models.CharField(choices=[('경기도', '경기도'), ('서울시', '서울시'), ('부산광역시', '부산광역시'), ('경상남도', '경상남도'), ('인천광역시', '인천광역시'), ('경상북도', '경상북도'), ('대구광역시', '대구광역시'), ('충청남도', '충청남도'), ('전라남도', '전라남도'), ('전라북도', '전라북도'), ('충청북도', '충청북도'), ('강원도', '강원도'), ('대전광역시', '대전광역시'), ('광주광역시', '광주광역시'), ('울산광역시', '울산광역시'), ('제주도', '제주도'), ('세종시', '세종시')], default='선택', max_length=100)),
                ('gender', models.CharField(choices=[('남자', '남자'), ('여자', '여자'), ('상관없음', '상관없음')], default='선택', max_length=20)),
                ('like_user', models.ManyToManyField(blank=True, related_name='like_care', to=settings.AUTH_USER_MODEL)),
                ('pet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='care_pet', to='accounts.pet')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('grade', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='care_review_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('care', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='care.care')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='care_comment_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
