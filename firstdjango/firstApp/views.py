from django.shortcuts import render, redirect
# import models
# Create your views here.
from django.http import HttpResponse
from firstApp.models import Student  # 导入
from django.contrib.auth import logout  # 需要导入


def test(request):
    return render(request, 'test.html')


def index(request):
    return HttpResponse(request, "hello,world!")


def student(request):
    if request.method == "POST":  # 判断请求为POST
        student = Student()  # 创建一个Student实例
        name = request.POST.get("name")  # 获取提交到表单的name
        age = request.POST.get("age")  # 获取提交到表单的age
        student.name = name  # 把值赋值给实例中的name 和age
        student.age = age
        student.save()  # 保存实例，把数据存进数据库
        return HttpResponse("学生信息提交成功！")  # 保存成功返回提示信息
    else:
        return render(request, 'detail.html')


# 位置参数
def show_news(request, a, b):
    """展示新闻界面"""
    return HttpResponse(F"现在展示的新闻界面：第{a}页, 第{b}行")


# 关键字参数
def show_news2(request, category, page_no):
    """展示新闻界面2"""
    return HttpResponse(F"现在展示的新闻界面：第{category}页，第{page_no}行")


# path 获取
def show_news3(request, category, page_no):
    """显示新闻界面3"""
    return HttpResponse(F"现在展示的新闻界面：第{category}页，第{page_no}行")


def home(request):
    account = request.session.get("account", default="未登录")  # 从session 中获取account 表示未登录
    return render(request, "home.html", {"account": account})


def login(request):
    if request.method == "GET":  # 如果是GET请求则返回登录界面
        path = request.GET.get("from")  # 获取url 路径中的form 参数
        return render(request, "login.html", {"path": path})
    else:  # 否则就是POST请求提交表单数据
        account = request.POST.get("account")  # 获取表单中的account 值
        passwd = request.POST.get("passwd")  # 获取表单中的passwd值
        path = request.GET.get("from")  # 获取url中from 参数，用来登录成功后跳转回登录前页面
        print(account)
        print(passwd)
        if account == "root" and passwd == "1111":  # 用户和密码匹配
            # 登录成功

            request.session["account"] = account  # 登录成功，设置session,下次访问就能辨别该用户
            return redirect('/home/')  # 跳转回home页面
        else:
            # 登录失败
            url = "/login/?from=%s" % (path)
            print(url)
            return redirect(url)  # 登录失败返回的还是登录界面


def quit(request):
    logout(request)  # 退出登录状态
    return redirect('/home')  # 返回home 页面
