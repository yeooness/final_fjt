from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('information', models.CharField(choices=[('반려동물 동반 식당', '반려동물 동반 식당'), ('반려동물 동반 카페', '반려동물 동반 카페'), ('동물병원', '동물병원')], default='선택', max_length=20)),
            ],
        ),
    ]
