from django.shortcuts import render,redirect,reverse
from .forms import UsersForm
from .models import *
from django.http import HttpResponse
import datetime
import time
from django.contrib.auth.hashers import check_password,make_password

# Create your views here.

def index(request):
    return render(request,'booktest/index.html')

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
        passsword = request.POST['password']
        password1 = request.POST['password1']
        if passsword == password1:
            if user.is_valid():
                user.save()
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

