from django.shortcuts import render,redirect,reverse
from .forms import UsersForm
from .models import *
from django.http import HttpResponse
import datetime
import time
from django.contrib.auth.hashers import check_password,make_password
from django.core.mail import send_mail,send_mass_mail
from django.conf import settings
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer,BadSignature,SignatureExpired
import io,random
from PIL import Image,ImageDraw,ImageFont
from django.views.decorators.cache import cache_page
from django.core.cache import cache

# Create your views here.

# @cache_page(60*15)
def index(request):
    messageinfos = MessageInfo.objects.all()
    hostpics = Hostpic.objects.all().order_by('index')

    result = cache.get("core")
    print(result)
    result = cache.set("core",123)
    print(result)
    result = cache.get("core")
    print(result)

    return render(request,'booktest/index.html',{"hostpics":hostpics,"messageinfos":messageinfos})

def login(request):
    return render(request,'booktest/reader_login.html',{"form":UsersForm()})

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        result = Users.objects.all().filter(username = username).filter(password = password)
        if len(result)>0:
            return redirect(reverse('booktest:reader',args=(result[0].id,)))
        return HttpResponse(result)
    else:
        return HttpResponse("登录失败")

def register(request):
    return render(request,'booktest/register.html',{"form":UsersForm()})

def user_register(request):
    if request.method == "POST":
        user = UsersForm(request.POST)
        username = request.POST['username']
        passsword = request.POST['password']
        password1 = request.POST['password1']
        email = request.POST['email']
        if passsword == password1:
            if user.is_valid():
                user = user.save(commit=False)
                user.is_active = False
                user.save()
                id = Users.objects.get(username=username).id
                # 1得到序列化工具
                serutil = Serializer(settings.SECRET_KEY, 60)
                result =  serutil.dumps({"userid":id}).decode("utf-8")
                send_mail("点击激活账户", "<a href='http://127.0.0.1:8000/booktest/active/%s'>点击链接激活账户</a>"%(result,),
                          settings.DEFAULT_FROM_EMAIL, [email])
                return redirect(reverse('booktest:login'))
            else:
                return HttpResponse("注册失败")
        else:
            return HttpResponse('密码不一致')
    else:
        return HttpResponse("注册失败")

def reader_query(request,id):
    user = Users.objects.get(pk=id)
    books = None
    if request.method == "POST":
        if request.POST['item'] == 'name':
            name = request.POST['query']
            books = Books.objects.all().filter(book_name= name)
        else:
            author = request.POST['query']
            books = Books.objects.all().filter(author= author)
    return render(request,'booktest/reader_query.html',{"user":user,"books":books})

def reader_info(request,id):
    user = Users.objects.get(pk=id)
    return render(request,'booktest/reader_info.html',{"user":user})

def reader_modify(request,id):
    user = Users.objects.get(pk=id)
    return render(request,'booktest/reader_modify.html',{"user":user})

def reader_updatemodify(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        college = request.POST['college']
        number = request.POST['number']
        email = request.POST['email']
        print("============================================",username)
        id = request.POST['id']
        user = Users.objects.get(pk=id)
        user.username = username
        if password:
            user.password = password
        user.college = college
        user.num = number
        user.email = email
        user.save()
        return redirect(reverse('booktest:reader_info',args=(id,)))

def reader_book(request,uid,bid):
    book = Books.objects.get(pk=bid)
    user = Users.objects.get(pk=uid)
    error =None
    if request.method == "GET":
        reader = Histroys.objects.all().filter(book_id=book)
        return render(request, 'booktest/reader_book.html', {"user": user, "book": book, "reader": reader})
    elif request.method == "POST":
        rea = Histroys.objects.all().filter(book_id=book)
        if rea:
            error = '已经被借阅了'
            return redirect(reverse('booktest:reader_book', args=(uid, bid,)))
        else:
            reader = Histroys()
            reader.book_id = book
            reader.user_id = user
            reader.user_name = user.username
            reader.date_return = time.strftime('%Y-%m-%d',time.localtime(time.time() + 2600000))
            reader.save()
            return redirect(reverse('booktest:reader_book',args=(uid,bid,)))
        # return render(request, 'booktest/reader_book.html', {"user": user, "book": book, "reader": reader})

def reader_histroy(request,uid):
    user = Users.objects.get(pk=uid)
    history = Histroys.objects.all().filter(user_id=user,status='return' )
    return render(request, 'booktest/reader_histroy.html', { "histroys": history,"user":user})

def reader(request,id):
    user = Users.objects.get(pk=id)
    return render(request,'booktest/reader.html',{"user":user})


def manager(request,id):
    admin = User.objects.get(pk=id)
    return render(request,'booktest/manager.html',{'admin':admin})

def manager_login(requset):
    if requset.method == 'GET':
        return render(requset,'booktest/manager_login.html')
    elif requset.method == 'POST':
        username = requset.POST['username']
        password = requset.POST['password']
        admin = User.objects.get(username=username)
        if check_password(password,admin.password):
            return redirect(reverse('booktest:manager',args=(admin.id,)))
        else:
            print(admin)
            error = '用户名或者密码不对'
            return render(requset,'booktest/manager_login.html',{'error':error})

def upload(request):
    if request.method == "GET":
        return render(request,'booktest/reader_upload.html')
    elif request.method == "POST":
        name = request.POST['name']
        index = request.POST['index']
        # 文件数据需要使用FILES 获取 enctype="multipart/form-data"
        pic = request.FILES['pic']
        hp = Hostpic(name=name,index=index,pic=pic)
        hp.save()
        return redirect(reverse('booktest:index'))

def edit(request):
    if request.method == "GET":
        return render(request,'booktest/edit.html')
    elif request.method == "POST":
        mname = request.POST["mname"]
        hcontent = request.POST["hcontent"]
        msg = MessageInfo(mname=mname,hcontent=hcontent)
        msg.save()
        return redirect(reverse('booktest:index'))

def mail(request):
    '''发送邮件'''
    try:
        send_mail("Django发送邮件", "<a href='http://127.0.0.1:8000/booktest/'>点击链接</a>",
                  settings.DEFAULT_FROM_EMAIL, ["1768804958@qq.com",])
    except Exception as e:
        return HttpResponse("发送失败")
    return HttpResponse("发送成功")

def active(request,idstr):
    # 1得到序列化工具
    serutil = Serializer(settings.SECRET_KEY,60)
    try:
        obj = serutil.loads(idstr)
        user = Users.objects.get(pk=obj["userid"])
        user.is_active = True
        user.save()
        return redirect(reverse('booktest:login'))
    except SignatureExpired :
        return HttpResponse("验证码失效了")

def ajax(request):
    return render(request,'booktest/ajax.html')

def ajaxa(request):
    if request.method == "GET":
        return HttpResponse("GET请求成功")
    elif request.method == "POST":
        return HttpResponse("POST请求成功")

def ajaxlogin(request):
    if request.method == "GET":
        return render(request,'booktest/ajaxlogin.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        verifycode = request.POST['verifycode']
        user = Users.objects.filter(username=username,password=password).first()
        if user is None:
            return HttpResponse('登录失败')
        else:
            if verifycode == request.session.get("verifycode"):
                return HttpResponse("登录成功")
            else:
                return HttpResponse("验证码错误")

def checkuser(request):
    if request.method == "POST":
        username = request.POST["username"]
        user = Users.objects.filter(username= username).first()
        if user is None:
            return HttpResponse("不存在该用户")
        else:
            return HttpResponse("存在该用户")

def verifycode(request):
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100),
               random.randrange(20, 100),
               random.randrange(20, 100))
    width = 100
    heigth = 25
    # 创建画面对象
    im = Image.new('RGB', (width, heigth), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0,100):
        xy = (random.randrange(0,width),random.randrange(0, heigth))
        fill = (random.randrange(0,255),255,random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    print(rand_str,'++++++++++')
    # 构造字体对象
    font = ImageFont.truetype('STXINGKA.TTF', 23)
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw

    # 将生产的验证码存入session
    request.session['verifycode'] = rand_str
    f = io.BytesIO()
    im.save(f, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(f.getvalue(), 'image/png')