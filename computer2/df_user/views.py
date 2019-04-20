from django.shortcuts import render, redirect
from hashlib import sha1  # 密码加密
from .models import UserInfo
import re
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from . import user_decorator


# Create your views here.


def register(request):
    return render(request, 'df_user/register.html', {'title': '用户注册'})


def register_handle(request):
    # 接收用户
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')

    count = UserInfo.objects.filter(uname=uname).count()  # count为0或1
    # return JsonResponse({'count': count})
    if count:
        return HttpResponse('该账号已经注册过，请登录')

    # 虽然js已经写了一遍验证，但是当网络不好或者其他原因时，会绕过前端的js验证，所以最好再加上后台验证

    # # 判断用户是否填写了信息
    # if not (uname and upwd and upwd2 and uemail):
    #     return redirect('/user/register/')
    #
    # #判断姓名长度
    # if len(uname)<5 or len(uname)>20:
    #     return redirect('/user/register/')
    # #
    # # #验证用户名是否已经存在
    # if UserInfo.objects.filter(uname=uname).count() != 0:
    #     return redirect('/user/register/')
    # #
    # #判断两次密码
    # if upwd != upwd2 or len(upwd) < 8 or len(upwd) > 20 :
    #     return redirect('/user/register/')
    #
    # # 验证邮箱
    # if re.match("^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$", uemail) == None:  # re.match匹配失败时返回None
    #     return redirect('/user/register/')

    # 密码加密
    s1 = sha1()
    s1.update(upwd.encode('utf-8'))  # 指定加密的字符串编码
    upwd3 = s1.hexdigest()  # 获得加密之后的结果

    # 创建对象，保存到数据库
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()

    # 注册成功，转到登录界面
    return redirect('/user/login/')


def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 0, 'uname': uname}
    return render(request, 'df_user/login.html', context)


def login_handle(request):
    # 接收登录信息
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    jizhu = post.get('jizhu', 0)  # 当jizhu有值时,即jizhu被勾选等于1时,返回的数据为1,否则get返回后面的0

    # 根据用户名查询对象
    users = UserInfo.objects.filter(uname=uname)  # 查询结果为一个列表
    # print(users)

    # 判断：如果未查到则说明用户名错误，如果查到则判断密码是否正确，如果密码正确，则返回用户中心
    if len(users) == 1:
        s1 = sha1()
        s1.update(upwd.encode("utf-8"))
        if s1.hexdigest() == users[0].upwd:
            return redirect('/goods/')
            # return HttpResponse('登录成功')
            # url = request.COOKIES.get('url', '/')  # 获取登录之前进入的页面,如果没有,则进入首页
            # red = HttpResponseRedirect(url)  # 用变量记住,方便设置cookie
            # # 记住用户名
            # if jizhu != 0:
            #     red.set_cookie('uname', uname)  # 设置cookie保存用户名
            # else:
            #     red.set_cookie('uname', '', max_age=-1)  # max_age指的是过期时间,当为-1时为立刻过期
            # request.session['user_id'] = users[0].id  # 把用户id和名字放入session中
            # request.session['user_name'] = uname
            # return red
        else:
            # return HttpResponse('密码错误')
            context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 1, 'uname': uname, 'upwd': upwd}
            return render(request, 'df_user/login.html', context)
    context = {'title': '用户登录', 'error_name': 1, 'error_pwd': 0, 'uname': uname, 'upwd': upwd}
    return render(request, 'df_user/login.html', context)
    # return HttpResponse('用户不存在')


@user_decorator.login
def logout(request):
    return HttpResponse('退出')


@user_decorator.login
def info(request):   # 个人信息
    # return HttpResponse('个人信息')
    return render(request, 'df_user/user_center_info.html', {})


@user_decorator.login
def order(request):   # 全部订单
    # return HttpResponse('订单')
    return render(request, 'df_user/user_center_order.html', {})


@user_decorator.login
def site(request):   # 收货地址
    # return HttpResponse('修改个人信息')
    return render(request, 'df_user/user_center_site.html', {})



