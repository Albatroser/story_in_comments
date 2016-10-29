from mysite.celery import app
from story_posting.models import Post


@app.task()
def post_story():
    for post in Post.objects.all():
        if post.is_posted and post.vk_id_real and not post.story.is_posted:
            print(post.text)
            post.post_story()
