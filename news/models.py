from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    content = models.TextField()
    photo = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
