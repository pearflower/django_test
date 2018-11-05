from django.http import HttpResponse


def my_decorator(view):
    def wrapper(request,*args,**kwargs):
        if request.META.get('REMOTE_ADDR') == '127.0.0.1':
            return HttpResponse('禁止访问')
        return view(request,*args,**kwargs)
    return wrapper
