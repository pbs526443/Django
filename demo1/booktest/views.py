from django.shortcuts import render
from django.http import  HttpResponse
from .models import BookInfo,HeroInfo
# Create your views here.

def index(request):
    print("请求",request)
    return HttpResponse('首页')


def list(request):

    return HttpResponse('列表页')

def detail(request,id,age):
    return HttpResponse('标签页'+'  '+str(id)+'  '+str(age))

def details(request,id):
    result = BookInfo.objects.get(pk=int(id)).btitle
    return HttpResponse(result)

'''
视图函数
将函数和路由绑定
'''