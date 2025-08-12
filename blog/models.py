from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    counted_view = models.IntegerField(default=0)
    staus = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
