from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=225)
    body = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    like_total = models.IntegerField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    def summary():
        return self.body[:100]
    def created_date():
        return self.created_date.strftime('%b %e %Y')

    # class Meta:
    #     ordering = ['-created_date']


class Comment(models.Model):
    blog= models.ForeignKey(
        Blog, on_delete=models.CASCADE, )
    comment_author = models.CharField(max_length=50)
    comment_content = models.CharField(max_length=200)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content

    # class Meta:
    #     ordering = ['-comment_date']
