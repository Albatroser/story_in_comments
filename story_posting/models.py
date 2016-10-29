from django.db import models
from glue.models import Community, Vkaccount


class Post(models.Model):
    text = models.CharField(max_length=300)
    community = models.ForeignKey(Community)
    is_posted = models.BooleanField(default=False)
    is_proposed = models.BooleanField(default=False)
    vk_id_request = models.IntegerField(null=True, blank=True)
    vk_id_real = models.IntegerField(null=True, blank=True)
    vkaccount = models.ForeignKey(Vkaccount)

    def post(self):
        self.vkaccount.api.method("wall.post", {
            "owner_id": -self.community.vk_domen,
            "message": self.text
        })


class Story(models.Model):
    name = models.CharField(max_length=300)
    post = models.ForeignKey(Post)

    def post(self):
        comments = self.comment_set.order_by("order")
        for comment in comments:
            comment.post()


class Comment(models.Model):
    text = models.CharField(max_length=300)
    vkaccount = models.ForeignKey(Vkaccount)
    order = models.IntegerField()
    story = models.ForeignKey(Story)

    def post(self):
        self.vkaccount.api.method("wall.createComment", {
            "owner_id": -self.story.post.community.vk_domen,
            "post_id": self.story.post.vk_id,
            "message": self.text,
        })
