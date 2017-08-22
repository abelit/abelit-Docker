from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import default_token_generator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.models import User
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from dataforum import settings
from django.core.mail import send_mail
import re
import random

# Create your views here.
# 首页
def index(request):
    return render(request, 'home/index.html')

# 登录
def login(request):
    # 获取请求的页面，登陆成功后跳转到改请求页面
    nextpage = request.GET.get('next', '/')

    # 如果用户已经登陆，跳转到用户需要请求的页面
    if request.user.is_authenticated:
        if nextpage == "/":
            return redirect("/")
        return redirect(nextpage)

    if request.method == 'POST':
        # 获取页面提交的用户名、密码、验证码
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # vcode = request.POST.get('vcode').upper()
        # vcode_session = request.session.get('verify_code').upper()
        username = request.POST['username']
        password = request.POST['password']
        verify_code = request.POST['verify_code'].upper()
        verify_code_session = request.session.get('verify_code').upper()

        # 判断用户名框输入的用户格式，如果是邮箱，那使用邮箱验证登陆，否则，则使用用户名登陆
        email_format = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
        is_email = bool(re.match(email_format,username,re.VERBOSE))
        if is_email:
            email = username
            user = User.objects.filter(email=email)
            # return HttpResponse(user)
            if user.exists():
                # username = user.values()[0]['username']
                username = user.get().username
            else:
                username=None

        # 使用Django认证模块认证用户
        user = auth.authenticate(username=username, password=password)
        result = {}
        if user is not None and user.is_active and verify_code == verify_code_session:
            # 登录
            auth.login(request, user)
            result = {'status': 'ok', 'message': '登陆成功！请稍后，页面正在跳转...'}
        elif verify_code != verify_code_session:
            result = {'status': 'no', 'message': '验证码输入错误！'}
        else:
            result = {'status': 'no', 'message': '用户名或密码错误！'}

        # 向页面返回json格式数据
        return JsonResponse(result)
    return render(request, 'home/login.html', {"nextpage": nextpage})

# 注册
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        verify_code = request.POST['verify_code'].upper()
        verify_code_session = request.session.get('verify_code').upper()

        db_user_byname = User.objects.filter(username=username)
        db_user_byemail = User.objects.filter(email=email)

        result = {}

        # 检查用户名是否已注册
        if db_user_byname.exists():
            return JsonResponse({'status': 'no', 'message': '用户已已被注册，请更换用户名！'})

        # 检查邮箱是否已注册
        if db_user_byemail.exists():
            return JsonResponse({'status': 'no', 'message': '该邮箱已被注册，请更换其他邮箱！'})

        if verify_code == verify_code_session:
            # 注册用户，把用户输入信息写入数据库
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            result = {'status': 'ok', 'message': '注册成功！请稍后，页面正在跳转...'}
        elif verify_code != verify_code_session:
            result = {'status': 'no', 'message': '验证码输入错误！'}
        else:
            result = {'status': 'no', 'message': '其他未知错误！'}

        return JsonResponse(result)
        # return HttpResponse("register page")
    return render(request, 'home/register.html')

# 退出
@login_required
def logout(request):
    auth.logout(request)
    return redirect('/accounts/login')

# # 忘记密码，发送邮件
# def forgot_password(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#
#         db_user_byemail = User.objects.filter(email=email)
#
#         # 如果该邮箱已经注册，则发送重置密码链接到改邮箱，否则返回错误
#         if not db_user_byemail.exists():
#             return JsonResponse({"status": "no", "message": email+"未被注册，请使用注册邮箱！"})
#
#         # 发送重置链接到邮件，并返回邮件发送状态
#         send_mail('重置密码','这里是重置密码链接。。。','ychenid@163.com',['ychenid@126.com'],fail_silently=False)
#         return JsonResponse({"status": "ok", "message": "重置密码链接已经发送到： "+email+" ，<br/>请登录您的邮箱点击重置密码链接！"})
#
#     return render(request, 'home/forgot_password.html')
#
# def reset_password(request):
#     username = "django"
#     password = 'cy123456'
#     # user = auth.authenticate(username=username, password=password)
#
#     user = User.objects.get(username=username)
#
#     db_password = user.password
#
#     tokens = default_token_generator.make_token(user)
#
#     result1 = default_token_generator.check_token(user,tokens)
#
#
#     return HttpResponse(db_password)


# 重置密码
@login_required
def change_password(request):
    if request.method == 'POST':
        password_old = request.POST['password_old']
        password = request.POST['password']

        username = request.user.username
        user = auth.authenticate(username=username, password=password_old)
        result = {}

        if user is not None:
            user.set_password(password)
            user.save()
            result = {"status": "ok", "message": "密码修改成功, 请重新登陆！"}
        else:
            result = {"status": "no", "message": "原密码不正确，请重新输入！"}

        return JsonResponse(result)

    return render(request, 'home/change_password.html')


def verify_code(request):
    # 1，定义变量，用于画面的背景色、宽、高
    # random.randrange(20, 100)意思是在20到100之间随机找一个数
    bgcolor = (random.randrange(20, 100), random.randrange(20, 100), 255)
    width = 100
    height = 25
    # 2，创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 3，创建画笔对象
    draw = ImageDraw.Draw(im)
    # 4，调用画笔的point()函数绘制噪点，防止攻击
    for i in range(0, 100):
        # 噪点绘制的范围
        xy = (random.randrange(0, width), random.randrange(0, height))
        # 噪点的随机颜色
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        # 绘制出噪点
        draw.point(xy, fill=fill)
    # 5，定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 6，随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 7，构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    # fontpath = "%s/fonts/roboto/Roboto-Medium.ttf" % (settings.STATICFILES_DIRS)
    fontpath = '{0}/{1}'.format(settings.STATIC_PATH,'fonts/roboto/Roboto-Medium.ttf')
    font = ImageFont.truetype(fontpath, 23)
    # 8，构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 9，绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 9，用完画笔，释放画笔
    del draw
    # 10，存入session，用于做进一步验证
    request.session['verify_code'] = rand_str
    # 11，内存文件操作
    buf = BytesIO()
    # 12，将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 13，将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


# test ajax
@login_required
def add(request):
    return render(request, 'home/testajax.html')

def add_ajax(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    # return HttpResponse(a)
    return HttpResponse(str(a+b))

# @csrf_exempt
def time_ajax(request):
    # c = request.POST['c']
    d = request.POST['d']
    c = request.POST.get('c')
    e = request.POST.get('e')
    # d = request.POST.get('d')
    c = int(c)
    d = int(d)
    e = int(e)
    return JsonResponse({"result":str(c*e)})

def ajax_list(request):
    a = range(100)
    return JsonResponse(json.dumps(a))

def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return JsonResponse(name_dict)

@login_required
def list_user(request):
    u = User.objects.all()

    return render(request, 'home/user.html', {"userlist":u})

def list_user_handler(request):
    pass
