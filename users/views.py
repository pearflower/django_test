import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

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


