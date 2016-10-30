

from django.shortcuts import render
from glue.models import Community
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
        communities_ids = request.POST.get("communities")
        messages = request.POST.get("message")
        comments_texts = request.POST.get("comments")

    return render(request, template, {})
