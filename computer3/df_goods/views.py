from django.shortcuts import render
from django.http import HttpResponse
from .models import Taishiji,Bijiben,Zhuban,Xianka,Cpu,Neicun,Yingpan,Jixiang,Yjxsq,Yinxiang,Shubiao,Jianpan
# Create your views here.


def index(request):
    goods = Cpu.objects.all()
    # print(goods)
    return render(request, 'df_goods/index.html', {'goods': goods})


def taishiji(request):
    goods = Taishiji.objects.all()
    return render(request, 'df_goods/taishiji.html', {'goods': goods})


def bijiben(request):
    goods = Bijiben.objects.all()
    return render(request, 'df_goods/bijiben.html', {'goods': goods})




