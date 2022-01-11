from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class Post(TimestampedModel):
    title = models.CharField(max_length=100)
    content = models.TextField()