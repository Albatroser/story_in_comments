from django.db import models
from glue.models import Community, Vkaccount


class Post(models.Model):
    text = models.CharField(max_length=300)
    community = models.ForeignKey(Community)
    is_posted = models.BooleanField(default=False)
    vk_id = models.IntegerField(null=True, blank=True)
    vkaccount = models.ForeignKey(Vkaccount)


class Story(models.Model):
    name = models.CharField(max_length=300)
    post = models.ForeignKey(Post)


class Comment(models.Model):
    text = models.CharField(max_length=300)
    vkaccount = models.ForeignKey(Vkaccount)
    order = models.IntegerField()
    story = models.ForeignKey(Story)
