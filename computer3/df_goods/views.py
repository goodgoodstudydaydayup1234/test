from django.shortcuts import render
from django.http import HttpResponse
from .models import Taishiji,Bijiben,Zhuban,Xianka,Cpu,Neicun,Yingpan,Jixiang,Yjxsq,Yinxiang,Shubiao,Jianpan
# Create your views here.


def index(request):
    goods = Cpu.objects.all()
    print(goods)
    return render(request, 'df_goods/index.html', {'goods': goods})







