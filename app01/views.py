from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def homepage(request):
    post = Post.objects.all()
    post_list = list()
    for count,post in enumerate(post):
        post_list.append("No.{}".format(str(count)+str(post)+'<br>'))
    return HttpResponse(post_list)

def homepage2(request):
    return render(request,'index.html')

from django.template.loader import get_template
from datetime import datetime

def homepage3(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

from django.shortcuts import redirect

def showpost(request,slug):
    template = get_template('post.html')
    now = datetime.now()
    try:
        post = Post.objects.get(slug=slug)
        if post is not None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')
