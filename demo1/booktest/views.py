from django.shortcuts import render
from django.http import  HttpResponse,HttpResponseRedirect
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

def bookadd(request):
    return render(request,'booktest/bookadd.html')

def addbook(request):
    btitle = request.POST['bookname']
    b1 = BookInfo()
    b1.btitle = btitle
    b1.save()
    return HttpResponseRedirect('/booktest/list/')

def bookupdate(request,bid):
    result = BookInfo.objects.get(pk=bid)
    return render(request,'booktest/bookupdate.html',{"book":result})

def updatebook(request):
    bookid = request.POST['bookid']
    btitle = request.POST['bookname']
    b1 = BookInfo.objects.get(pk=bookid)
    b1.btitle = btitle
    b1.save()
    return HttpResponseRedirect('/booktest/list/')

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

def delete(request,id):
    try:
        BookInfo.objects.get(pk=id).delete()
        result = BookInfo.objects.all()
        # 使用render没有刷新请求url
        # return render(request, 'booktest/list.html', {"booklist": result})
        # 重新向服务器发起请求 刷新url
        return HttpResponseRedirect('/booktest/list/',{'booklist':result})
    except Exception as e:
        return HttpResponse("删除失败")

def heroadd(request,bookid):
    return render(request,'booktest/heroadd.html',{'bookid':bookid})

def heroinfoadd(request):
    hname = request.POST['heroname']
    hsex = request.POST['sex']
    hcontent = request.POST['herocontent']
    bookid = request.POST['bookid']

    book  = BookInfo.objects.get(pk=bookid)
    h1 = HeroInfo()
    h1.hname = hname
    h1.hcontent = hcontent
    if hsex == 0:
        h1.hgender = False
    else:
        h1.hgender = True
    h1.hbook = book
    h1.save()

    # return render(request, 'booktest/detail.html', {"Bookdata":book})
    return HttpResponseRedirect('/booktest/details/'+str(bookid)+'/',{"Bookdata":book})
    # print(hname,hsex,hcontent,bookid)
    # return HttpResponse('添加成功')

def herodelete(request,hid):
    hero = HeroInfo.objects.get(pk=hid)
    bookid = hero.hbook
    # print(bookid)
    HeroInfo.objects.get(pk=hid).delete()
    book = BookInfo.objects.get(btitle=bookid)
    bookid = book.id
    # return HttpResponse(bookid)
    return HttpResponseRedirect('/booktest/details/' + str(bookid) + '/')

def heroupdate(request,hid):
    result = HeroInfo.objects.get(pk=hid)

    return render(request,'booktest/heroupdate.html',{"hero":result})

def addheroinfo(request):
    hname = request.POST['heroname']
    hgender = request.POST['sex']
    hcontent = request.POST['herocontent']
    hbook = request.POST['hbook']
    hid = request.POST['heroid']

    h1 = HeroInfo.objects.get(pk=hid)
    h1.hname = hname
    h1.hgender = hgender
    h1.hcontent = hcontent
    book = BookInfo.objects.get(btitle=hbook)
    h1.hbook = book
    h1.save()
    return HttpResponseRedirect('/booktest/details/' + str(book.id) + '/')





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