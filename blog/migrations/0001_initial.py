# Generated by Django 4.2.11 on 2024-04-14 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок поста')),
                ('body', models.TextField(verbose_name='содержимое')),
                ('preview_image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='превью')),
                ('slug', models.CharField(blank=True, max_length=150, null=True, verbose_name='slug')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='дата создания поста')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('view_count', models.IntegerField(default=0, verbose_name='просмотры')),
            ],
            options={
                'verbose_name': 'пост',
                'verbose_name_plural': 'посты',
            },
        ),
    ]
