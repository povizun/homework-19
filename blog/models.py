from django.db import models

NULLABLE = {'blank': True, 'null': True}


class BlogPost(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок поста')
    body = models.TextField(verbose_name='содержимое')
    preview_image = models.ImageField(verbose_name='превью', **NULLABLE)
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    created_at = models.DateField(auto_now_add=True, verbose_name='дата создания поста')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    view_count = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

