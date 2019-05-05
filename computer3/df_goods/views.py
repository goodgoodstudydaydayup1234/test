from django.shortcuts import render
from django.http import HttpResponse
from .models import Type,Taishiji,Bijiben,Zhuban,Xianka,Cpu,Neicun,Yingpan,Jixiang,Yjxsq,Yinxiang,Shubiao,Jianpan
# Create your views here.


def index(request):
    goods = Cpu.objects.all()
    # print(goods)
    return render(request, 'df_goods/index.html', {'goods': goods})


def singlei(request, id):
    single = Cpu.objects.get(pk=id)
    single.cclick += 1
    single.save()
    return render(request, 'df_goods/singlec.html', {'single': single})


def taishiji(request):
    goods = Taishiji.objects.all()
    return render(request, 'df_goods/taishiji.html', {'goods': goods})


def taishiji_huashuo(request):
    good1 = Taishiji.objects.get(pk=1)
    good2 = Taishiji.objects.get(pk=2)
    goods = [good1,good2]
    return render(request, 'df_goods/list.html', {'goods': goods})


def taishiji_lianxiang(request):
    good1 = Taishiji.objects.get(pk=3)
    goods = [good1]
    return render(request, 'df_goods/list.html', {'goods': goods})


def taishiji_daier(request):
    good1 = Taishiji.objects.get(pk=4)
    goods = [good1]
    return render(request, 'df_goods/list.html', {'goods': goods})


def taishiji_pingguo(request):
    good1 = Taishiji.objects.get(pk=5)
    good2 = Taishiji.objects.get(pk=6)
    good3 = Taishiji.objects.get(pk=7)
    goods = [good1, good2, good3]
    return render(request, 'df_goods/list.html', {'goods': goods})


def single(request, id):
    good = Taishiji.objects.get(pk=id)
    return render(request, 'df_goods/single.html', {'single': good})


def bijiben(request):
    goods = Bijiben.objects.all()
    return render(request, 'df_goods/bijiben.html', {'goods': goods})


def bijiben_huashuo(request):
    good1 = Bijiben.objects.get(pk=7)
    good2 = Bijiben.objects.get(pk=8)
    good3 = Bijiben.objects.get(pk=9)
    good4 = Bijiben.objects.get(pk=10)
    good5 = Bijiben.objects.get(pk=11)
    goods = [good1,good2, good3, good4, good5]
    return render(request, 'df_goods/list1.html', {'goods': goods})


def bijiben_lianxiang(request):
    good1 = Bijiben.objects.get(pk=1)
    good2 = Bijiben.objects.get(pk=2)
    good3 = Bijiben.objects.get(pk=3)
    good4 = Bijiben.objects.get(pk=4)
    good5 = Bijiben.objects.get(pk=5)
    good6 = Bijiben.objects.get(pk=6)
    goods = [good1, good2, good3, good4, good5, good6]
    return render(request, 'df_goods/list1.html', {'goods': goods})


def bijiben_daier(request):
    good1 = Bijiben.objects.get(pk=4)
    goods = [good1]
    return render(request, 'df_goods/list1.html', {'goods': goods})


def bijiben_pingguo(request):
    good1 = Bijiben.objects.get(pk=12)
    good2 = Bijiben.objects.get(pk=13)
    good3 = Bijiben.objects.get(pk=14)
    good4 = Bijiben.objects.get(pk=15)
    goods = [good1, good2, good3, good4]
    return render(request, 'df_goods/list1.html', {'goods': goods})


def single1(request, id):
    good = Bijiben.objects.get(pk=id)
    return render(request, 'df_goods/single1.html', {'single': good})


def cpu(request):
    goods = Cpu.objects.all()
    return render(request, 'df_goods/zjyj_cpu.html', {'goods': goods})


def singlec(request, id):
    single = Cpu.objects.get(pk=id)
    return render(request, 'df_goods/singlec.html', {'single': single})


def zhuban(request):
    goods = Zhuban.objects.all()
    return render(request, 'df_goods/zjyj_zhuban.html', {'goods': goods})


def singlez(request, id):
    single = Zhuban.objects.get(pk=id)
    return render(request, 'df_goods/singlez.html', {'single': single})


def xianka(request):
    goods = Xianka.objects.all()
    return render(request, 'df_goods/zjyj_xianka.html', {'goods': goods})


def singlex(request, id):
    single = Xianka.objects.get(pk=id)
    return render(request, 'df_goods/singlex.html', {'single': single})


def yingpan(request):
    goods = Yingpan.objects.all()
    return render(request, 'df_goods/zjyj_yingpan.html', {'goods': goods})


def singley(request, id):
    single = Yingpan.objects.get(pk=id)
    return render(request, 'df_goods/singley.html', {'single': single})


def jixiang(request):
    goods = Jixiang.objects.all()
    return render(request, 'df_goods/yjws_jixiang.html', {'goods': goods})


def singlej(request, id):
    single = Jixiang.objects.get(pk=id)
    return render(request, 'df_goods/singlej.html', {'single': single})


def gouwuche(request):
    return HttpResponse('购物车')


# def list(request, id):
#     iddict = {'1':Taishiji,'2':Bijiben,3:Zhuban,4:Xianka,5:Cpu,6:Neicun,7:Yingpan,8:Jixiang,9:Yjxsq,10:Shubiao,11:Jianpan,12:Yinxiang}
#     print(iddict[1], type(iddict[1]))
#     goods = iddict[id].objects.all()
#     return render(request, 'df_goods/list.html', {'goods': goods})


def list(request):
    goods = Bijiben.objects.all()
    return render(request, 'df_goods/list1.html', {'goods': goods})

