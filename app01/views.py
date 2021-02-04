from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def homepage(request):
    post = Post.object.all()
    post_list = post()
    for count,post in enumerate(post):
        post_list.append("No.{}".format(str(count)+str(post)+'<br>'))
    return HttpResponse(post_list)
