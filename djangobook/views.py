#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse,Http404
# from django.shortcuts import render_to_response
import datetime
from django.shortcuts import render_to_response


def hello(request):#每一个视图函数都至少传递一个参数而且是第一个参数是HttpResponse类型的，这个对象也是HttpResponse类型的，返回
                   #也是一个HttpResponse的对象
                   #这个函数也只是一个普通的函数,没有继承任何的类
    return HttpResponse("Hello world")#注意这里HttpResponse()这个对象里面参数是一个字符串


def current_datetime(request):#添加一个动态的页面，但是要注意哪些是纯python的，哪些是具有Django特性的
    now = datetime.datetime.now()
    html = "<html><body>It is now %s</body></html>" % now
    return HttpResponse(html)


def current_datetime_tem(request):
    # now = datetime.datetime.now()
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime_tem.html',locals())#第一个参数是模板的字符串名字，第二个参数是一个字典


def hours_ahead(request,offset):#所以这里也是通过正则表达式传递过来一个参数，也就是说视图函数是可以接受多个参数的
    try:
        offset = int(offset)#传递过来的时候是正则表达式的字符串,应该是这么理解的，然后将其转化为整型
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)#使用timedelta的时候注意上面一层是一个包，而是datetime类
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    assert False  #这个显示局部变量的方法是不是Django内置的呢？先暂时不论，但是这个东西显示哪一些局部变量是显示的是以这条语句以上的局部变量
    return HttpResponse(html)

