from django.db import models
from pytils.translit import slugify

from config import settings
from users.models import NULLABLE, User


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.CharField(max_length=200, unique=True, **NULLABLE, db_index=True, verbose_name='url')
    content = models.TextField(verbose_name='content')
    preview = models.ImageField(upload_to='blog_images/', **NULLABLE, verbose_name='image')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='created_on')
    is_published = models.BooleanField(default=True, verbose_name='is_published')
    views = models.IntegerField(default=0, verbose_name='views')

    author = models.ForeignKey(settings.AUTH_USER_MODEL, **NULLABLE,
                               on_delete=models.SET_NULL, verbose_name='author')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'
        ordering = ('title', 'created_on', 'is_published',)
