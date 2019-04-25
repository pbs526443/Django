from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import *
from django.db.models import Q

# Create your views here.

def index(request):
    artis = article.objects.all()
    for art in artis:
        art.text = art.text[0:100]
    return render(request,'blog/index.html',{"artis":artis})

def index_action(request,cid):
    artis = cation.objects.get(pk=cid).article_set.all()
    for art in artis:
        art.text = art.text[0:100]
    return render(request,'blog/index.html',{"artis":artis,})

def index_tag(request,tid):
    artis = tag.objects.get(pk=tid).article_set.all()
    for art in artis:
        art.text = art.text[0:100]

    return render(request,'blog/index.html',{"artis":artis,})

def single_hr(request,aid):
    artis = article.objects.get(pk=aid)
    artis.number = artis.number + 1
    artis.save()
    return HttpResponseRedirect("/blog/single/"+str(aid)+"/")

def single(request,aid):
    artis = article.objects.get(pk=aid)
    return render(request, 'blog/single.html',{"artis": artis})

def addcomm(request):
    name = request.POST['name']
    email = request.POST['email']
    url = request.POST['url']
    content = request.POST['comment']
    aid = request.POST['aid']
    con = comment()
    con.username = name
    con.email = email
    con.website = url
    con.content = content
    con.artid = article.objects.get(pk=aid)
    con.save()
    return HttpResponseRedirect("/blog/single/"+aid+"/")

def index_time(request,year,month):
    artis = article.objects.all().filter(time_creation__year=year).filter(time_creation__month=month).order_by('-time_creation')
    for art in artis:
        art.text = art.text[0:100]
    return render(request,'blog/index.html',{"artis":artis,})