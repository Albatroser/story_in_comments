import time
from django.db import models
from glue.models import Community, Vkaccount


class Post(models.Model):
    text = models.TextField()
    community = models.ForeignKey(Community)
    is_posted = models.BooleanField(default=False)
    is_proposed = models.BooleanField(default=False)
    vk_id_request = models.IntegerField(null=True, blank=True)
    vk_id_real = models.IntegerField(null=True, blank=True)
    vkaccount = models.ForeignKey(Vkaccount)

    story_posted = models.BooleanField(default=False)
    ready_for_posting = models.BooleanField(default=False)

    def post(self):
        self.vkaccount.api.method("wall.post", {
            "owner_id": -self.community.vk_domen,
            "message": self.text,
            "attachments": "photo248870261_456239032",
        })
        self.is_proposed = True
        self.save()

    def post_story(self):
        self.story.post()
        self.story_posted = True

    def save(self):
        self.vkaccount = Vkaccount.objects.order_by("?")[0]
        super().save()

    def __str__(self):
        return self.text


class Story(models.Model):
    name = models.CharField(max_length=300, default="")
    parent_post = models.OneToOneField(Post, related_name='story')
    is_posted = models.BooleanField(default=False)

    def post(self):
        comments = self.comment_set.order_by("order")
        comment_id_to_reply = 0
        for comment in comments:
            # KPACUBO!
            comment_id_to_reply = comment.post(comment_id_to_reply)
            time.sleep(1.5)

        self.is_posted = True
        self.save()

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    vkaccount = models.ForeignKey(Vkaccount)
    order = models.IntegerField()
    story = models.ForeignKey(Story)

    def post(self, comment_id_to_reply):
        response = self.vkaccount.api.method("wall.createComment", {
            "owner_id": -self.story.parent_post.community.vk_domen,
            "post_id": self.story.parent_post.vk_id_real,
            "message": self.text,
            "reply_to_comment": comment_id_to_reply
        })
        return response["comment_id"]

    def save(self):
        if self.order % 2 == 0:
            self.vkaccount = Vkaccount.objects.all()[0]
        else:
            self.vkaccount = Vkaccount.objects.all()[1]

        super().save()

    def __str__(self):
        return self.text
