from django.shortcuts import render
from apps.home.models import Post 


def home_page(request):
    posts = Post.objects.all()

    return render(request, "home.html", context={"posts": posts})