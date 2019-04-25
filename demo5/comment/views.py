from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.http import HttpResponse
from .forms import CommentForm
from blog.models import article
# Create your views here.

def commitcomment(request,id):
    art = get_object_or_404(article,pk=id)
    if request.method == "POST":
        comment = CommentForm(request.POST)
        if comment.is_valid():
            comment = comment.save(commit=False)
            comment.artid =art
            comment.save()
            return redirect(reverse('blog:single',args=(id,)))
        else:
            return HttpResponse("评论失败")
    else:
        return HttpResponse("评论失败")