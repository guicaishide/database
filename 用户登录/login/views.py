from django.shortcuts import render
from django.http.response import HttpResponse
from .form import *

# Create your views here.

def bookform(request):
    if request.method=='GET':
        book = BookForm()
        return render(request,'data_form.html',locals())

    else:
        book = BookForm(request.POST)
        if book.is_valid():
            book.save()
            return HttpResponse('added successfully')
        else:
            error_msg=book.errors.as_json()
            return render(request,'data_form.html',locals())

def authorform(request):
    if request.method=='GET':
        author=AthorForm()
        return render(request,'author_form.html',locals())
    else:
        author=AthorForm(request.POST)
        if author.is_valid():
            author.save()
            return HttpResponse('added successfully')
        else:
            error_msg=author.errors.as_json()
            return render(request,'author_form.html',locals())

def publishform(request):

    if request.method=='GET':
        publish=PublishForm()
        return render(request,'publish_form.html',locals())
    else:
        publish=PublishForm(request.POST)
        if publish.is_valid():
            publish.save()
            return HttpResponse('added successfully')
        else:
            error_msg=publish.errors.as_json()
            return render(request,'publish_form.html',locals())

def show(request):
    #从Book 模型中取出需要展示的字段
    book_list=Book.objects.values('title','publishDate','price','pageNum','publish','authors')
    for book in book_list:
        # 根据外键的id，查询到对应的object对象
        publish=Publish.objects.filter(nid=book['publish'])
        authors=Author.objects.filter(nid=book['authors'])
        # 更新book_list,更新外键字段
        book['publish']=publish[0].name
        book['authors']=authors[0].name
    return render(request,'show.html',locals())