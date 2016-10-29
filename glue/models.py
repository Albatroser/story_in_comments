from django.db import models


class Community(models.Model):
    vk_domen = models.IntegerField()
    name = models.CharField(max_length=300, default="")
    url = models.CharField(max_length=300, default="")


class Post(models.Model):
    text = models.CharField(max_length=300)
    community = models.ForeignKey(Community)
    is_posted = models.BooleanField(default=False)
    vk_id = models.IntegerField(null=True, blank=True)


class Story(models.Model):
    name = models.CharField(max_field=300)
    post = models.ForeignKey(Post)


class Comment(models.Model):
    text = models.CharField(max_length=300)
    order = models.IntegerField()
    story = models.ForeignKey(Story)
