import json

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import View

# Create your views here.
from django.utils.encoding import smart_str

from users import tools
from users.decorators import my_decorator


@my_decorator
def index(request):
    return render(request,'index.html')

def goods(request,page,cate):
    print(request.GET.getlist('a'))
    print(request.GET.get('b'))

    return HttpResponse('cate:%s\npage:%s'%(cate,page))

def news(request):
    post_username = request.POST.get('username')
    post_password = request.POST.get('password')

    try:
        json_data = json.loads(request.body.decode())
        nick_name = json_data.get('nickname')
        age = json_data.get('age')
    except Exception as e:
        nick_name = None
        age = None

    return HttpResponse('username:%s\npassword:%s\nnickname:%s\nage:%s'%(post_username,post_password,nick_name,age))

def getheader(request):
    ip = request.META.get('REMOTE_ADDR')
    host = request.META.get('REQUEST_METHOD')
    content_length = request.META.get('CONTENT_LENGTH')

    # 自定义请求头
    abc = request.META.get('HTTP_ABC')

    return HttpResponse('ip:%s\nhost:%s\nlength:%s\nabc:%s'%(ip,host,content_length,abc))

def common_resp(request):
    '''返回普通的response对象'''
    resp = HttpResponse('CommonResp你好啊',status=203,content_type='text/html;charset=utf-8')
    return resp

def json_resp(request):
    '''返回json对象'''
    resp = JsonResponse([{"a":"1","b":"2","名字":"小王八"},{"name":"cristina"}],content_type='application/json;charset=utf-8',safe=False)
    return resp

def redirect_page(request):
    return HttpResponseRedirect('/users/index')

def set_cookie(request):
    resp = HttpResponse('保存cookie成功',content_type='text/html;charset=utf-8')
    resp.set_cookie('username',tools.convert_str2_iso('小王八'))
    # resp.set_cookie('username','小王八')
    resp.set_cookie('userid',11)
    return resp

def get_cookie(request):
    return HttpResponse(tools.convert_str2_utf(request.COOKIES.get('username'))+request.COOKIES.get('userid'))

def set_session(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    request.session['username'] = username
    request.session['password'] = password

    return HttpResponse('保存session成功')

def get_session(request):
    if request.method.lower() == 'get':
        username = request.session.get('username')
        password = request.session.get('password')
    elif request.method.lower() == 'post':
        username = request.POST.get('username')
        password = request.POST.get('password')
    return HttpResponse(username+password)


class MyView(View):

    def get(self,request):
        return render(request,'index.html')

    def post(self,request):
        userid = request.POST.get('userid')
        return HttpResponse('userid:'+str(userid))

