# Generated by Django 3.2.11 on 2022-01-13 11:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('region', models.CharField(db_index=True, max_length=10, verbose_name='지역')),
                ('city', models.CharField(db_index=True, max_length=10, verbose_name='도시')),
                ('charming', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(5)], verbose_name='귀여움')),
                ('name', models.CharField(db_index=True, max_length=10, verbose_name='이름')),
                ('explain', models.TextField(verbose_name='설명')),
                ('photo', models.ImageField(upload_to='mascot/character/%Y/%M/%d', verbose_name='사진')),
            ],
            options={
                'verbose_name': '마스코트',
                'verbose_name_plural': '마스코트 목록',
            },
        ),
    ]