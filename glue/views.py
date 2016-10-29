from django.shortcuts import render
from glue.models import Community
from django.contrib.auth.decorators import login_required


@login_required()
def communities(request):
    template = "glue/main.html"
    communities = Community.objects.all()
    return render(request, template, {"communities": communities})
