from mysite.celery import app
from story_posting.models import Post


@app.task()
def post_things():
    for post in Post.objects.all():
        if not post.ready_for_posting:
            print("post is not ready %s" % post.text)
            continue

        if post.is_posted and post.vk_id_real and not post.story.is_posted:
            print("posting story to community %s" % post.text)
            post.post_story()

        if not post.is_proposed:
            print("posting post to community %s" % post.text)
            post.post()
