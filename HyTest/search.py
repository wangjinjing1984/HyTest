# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response   #引入response解析

#表单
def search_form(request):
    return render_to_response('search_form.html')


#服务端 接受请求数据
def search(request):
    request.encode = 'utf-8'
    if 'q' in request.GET:
        message = '你搜索的内容为:' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)