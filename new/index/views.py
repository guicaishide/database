from django.shortcuts import render
from .forms import *
from .models import *
from django.http.response import HttpResponse

# Create your views here.
def write_database_icoView(request):
    if request.method =='GET':
        account = AccountForm()
        return render(request,'write_database_ico.html',locals())
    else:
        account = AccountForm(request.POST,request.FILES)
        if account.is_valid():
            account.save()
            return HttpResponse('success')
        else:
            return HttpResponse('fail')

def write_2View(request):
    if request.method =='GET':
        left = LeftForm()
        return render(request,'write_2.html',locals())
    else:
        left = LeftForm(request.POST)
        if left.is_valid():
            left.save()
            return HttpResponse('success')
        else:
            return HttpResponse('fail')
def write_3View(request):
    if request.method =='GET':
        left = LeftMiddleForm(request.FILES)
        return render(request,'write_2.html',locals())
    else:
        left = LeftMiddleForm(request.POST)
        if left.is_valid():
            left.save()
            return HttpResponse('success')
        else:
            return HttpResponse('fail')
def write_4View(request):
    if request.method =='GET':
        left = ArticleModelForm()
        return render(request,'write_4.html',locals())
    else:
        left = ArticleModelForm(request.POST,request.FILES)
        print('111')
        if left.is_valid():
            left.save()
            return HttpResponse('success')
        else:
            return HttpResponse('fail')

def indexView(request):
    photo=AccountModel.objects.filter(id=2)
    number=photo[0].number
    news=photo[0].news
    new_number=photo[0].new_number
    function_list=LeftModel.objects.values('name')
    function_middle_list=LeftMiddleModel.objects.filter(type='功能')
    function_manage_list = LeftMiddleModel.objects.filter(type='管理')
    function_ad_list = LeftMiddleModel.objects.filter(type='推广')
    function_count_list = LeftMiddleModel.objects.filter(type='统计')
    function_set_list = LeftMiddleModel.objects.filter(type='设置')
    function_python_list = LeftMiddleModel.objects.filter(type='开发')
    account_list = LeftMiddleModel.objects.filter(type='账号整体情况')

    myfile_list=ArticleModel.objects.values('title','pic','time','read','looking','comment','share')

    return  render(request,'index.html',locals())