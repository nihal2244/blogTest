from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=225)
    url = models.URLField()
    created_at = models.DateField(auto_now_add=True)
    like_total = models.IntegerField()
    body = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, verbose_name="Makale", related_name="comments")
    comment_author = models.CharField(max_length=50, verbose_name="İsim")
    comment_content = models.CharField(max_length=200, verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']
