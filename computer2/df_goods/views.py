from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import TypeInfo, GoodsInfo
# Create your views here.


def index(request):
    # 查询各分类的最新4条,最热4条信息
    type = TypeInfo.objects.get(pk=2)  # 首先获得外键指向的表中对象，然后通过‘_set’这样的方法获得目标表中的数据
    # print(type)
    goods = type.goodsinfo_set.filter(gbrand='华硕').all()
    # print(goods)
    # type0 = typelist[11].goodsinfo_set.order_by('-id')[:]  # 按降序获得,获得最大的
    # type01 = typelist[11].goodsinfo_set.order_by('-gclick')[:]
    # print(type0)
    # print('+++++++++++++++',type0[0], type(type0[0]), type0[0].gpicb1)
    # print(type0[1])
    # print(type0[2])
    # print(type0[3])
    # print('+++++++++++++++',type0[4])
    # print(type01)
    # type1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    # type11 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]
    # type2 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    # type21 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]
    # type3 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    # type31 = typelist[3].goodsinfo_set.order_by('-gclick')[0:4]
    # type4 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    # type41 = typelist[4].goodsinfo_set.order_by('-gclick')[0:4]
    #
    # context = {
    #     'title': '首页',
    #     'type0': type0, 'type01': type01,
    #     'type1': type1, 'type11': type11,
    #     'type2': type2, 'type21': type21,
    #     'type3': type3, 'type31': type31,
    #     'type4': type4, 'type41': type41,
    # }
    # print(context)
    # goods = GoodsInfo.objects.get(pk=1)
    return render(request, 'df_goods/index.html', {'goods': goods})


def taishiji(request):
    # return HttpResponse('taishiji')
    type = TypeInfo.objects.get(pk=1)
    goods = type.goodsinfo_set.all()
    # print(goods)
    return render(request, 'df_goods/taishiji.html', {'goods': goods})


def taishijihuoshuo(request):
    # return HttpResponse('huashuo')
    type = TypeInfo.objects.get(pk=1)
    goods = type.goodsinfo_set.filter(gbrand='华硕').all()
    return render(request, 'df_goods/list.html', {'goods': goods})


def taishijilianxaing(request):
    # return HttpResponse('huashuo')
    type = TypeInfo.objects.get(pk=1)
    goods = type.goodsinfo_set.filter(gbrand='联想').all()
    return render(request, 'df_goods/list.html', {'goods': goods})


def taishijidaier(request):
    # return HttpResponse('huashuo')
    type = TypeInfo.objects.get(pk=1)
    goods = type.goodsinfo_set.filter(gbrand='戴尔').all()
    return render(request, 'df_goods/list.html', {'goods': goods})


def taishijipingguo(request):
    # return HttpResponse('huashuo')
    type = TypeInfo.objects.get(pk=1)
    goods = type.goodsinfo_set.filter(gbrand='苹果').all()
    return render(request, 'df_goods/list.html', {'goods': goods})


def single(request, id):
    # return HttpResponse('single')
    single = GoodsInfo.objects.get(pk=id)
    return render(request, 'df_goods/single.html', {'single': single})


def bijiben(request):
    # return HttpResponse('bijiben')
    type = TypeInfo.objects.get(pk=2)
    goods = type.goodsinfo_set.all()
    return render(request, 'df_goods/bijiben.html', {'goods': goods})


def gouwuche(request,id):
    single = GoodsInfo.objects.get(pk=id)
    # return render(request, 'df_goods/gouwuche.html', {'single': single})
    return HttpResponse('gouwuche')

