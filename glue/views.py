

from django.shortcuts import render
from glue.models import Community
from story_posting.models import Post, Story, Comment
from django.contrib.auth.decorators import login_required


from django.views.decorators.csrf import csrf_protect


@login_required()
def communities(request):
    template = "glue/main.html"
    communities = Community.objects.all()
    return render(request, template, {"communities": communities})


@csrf_protect
@login_required()
def adding(request):
    template = "glue/adding.html"
    if request.method == 'POST':
        communities_urls = request.POST.getlist("communities[]")
        message = request.POST.get("message")
        comments_texts = request.POST.getlist("comments[]")

        communities = [Community.objects.get_or_create(url=url) for url in communities_urls]
        for community in communities:
            community.save()
            post = Post(text=message, community=community)
            post.save()

            story = Story(parent_post=post)
            story.save()

            for i in range(len(comments_texts)):
                comment = Comment(text=comments_texts[i], order=i + 1, story=story)
                comment.save()

            post.ready_for_posting = True
            post.save()

    return render(request, template, {})
