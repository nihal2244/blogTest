from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=225,null=True,blank=True)
    body = models.TextField(null=True,blank=True)
    posted_on =  models.DateTimeField(null=True)
    like_total = models.IntegerField(default=0)
    views_total = models.IntegerField(default=0)
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True,)

    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:100]
    def created_date(self):
        return self.created_date.strftime("%b %e %Y")

    class Meta:
        ordering = ['-posted_on']


class Comment(models.Model):
    blog= models.ForeignKey(
        Blog, on_delete=models.CASCADE,related_name="comments")
    comment_author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    comment_content = models.CharField(max_length=200)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']
