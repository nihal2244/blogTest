# Generated by Django 2.2.6 on 2019-10-31 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_blog_posted_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='views_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='blog',
            name='like_total',
            field=models.IntegerField(default=0),
        ),
    ]
