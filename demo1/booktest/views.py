from django.shortcuts import render
from django.http import  HttpResponse
from .models import BookInfo,HeroInfo
from django.template import loader
# Create your views here.

# 定义视图函数
def index(request):
    # print("请求",request)
    # return HttpResponse('首页')
    # indextem = loader.get_template('booktest/index.html')
    # cont = {"username":"pbs"}
    # # 使用变量参数渲染模板
    # result = indextem.render(cont)
    # # 返回模板
    # return HttpResponse(result)
    return render(request,'booktest/index.html',{"username":"pbs"})


def list(request):
    # return HttpResponse('列表页')
    result = BookInfo.objects.all()
    return render(request,'booktest/list.html',{"booklist":result})

def detail(request,id,age):
    # return HttpResponse('标签页'+'  '+str(id)+'  '+str(age))
    return render(request,'booktest/list.html')

def details(request,id):
    # try:
    #     result = BookInfo.objects.get(pk=int(id)).btitle
    #     return HttpResponse(result)
    # except Exception as e:
    #     print(e)
    result = BookInfo.objects.get(pk=id)
    return render(request,'booktest/detail.html',{"Bookdata":result})


'''
视图函数
将函数和路由绑定
'''

'''
创建模板文件夹 templates
配置模板目录 os.path.join(BASEDIR,'templates')
创建项目模板目录，创建模板

加载模板 loader.get_template()
使用变量渲染模板  result = temp.render({})
返回模板 HttpResponse(result)
'''