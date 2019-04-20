from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import TypeInfo, GoodsInfo
# Create your views here.


def index(request):
    # 查询各分类的最新4条,最热4条信息
    typelist = TypeInfo.objects.all()  # 首先获得外键指向的表中对象，然后通过‘_set’这样的方法获得目标表中的数据
    print(typelist)
    type0 = typelist[11].goodsinfo_set.order_by('-id')[:]  # 按降序获得,获得最大的
    type01 = typelist[11].goodsinfo_set.order_by('-gclick')[:]
    print(type0)
    print('+++++++++++++++',type0[0], type(type0[0]), type0[0].gpicb1)
    print(type0[1])
    print(type0[2])
    print(type0[3])
    print('+++++++++++++++',type0[4])
    print(type01)
    type1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]
    type2 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    type21 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]
    type3 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    type31 = typelist[3].goodsinfo_set.order_by('-gclick')[0:4]
    type4 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    type41 = typelist[4].goodsinfo_set.order_by('-gclick')[0:4]

    context = {
        'title': '首页',
        'type0': type0, 'type01': type01,
        'type1': type1, 'type11': type11,
        'type2': type2, 'type21': type21,
        'type3': type3, 'type31': type31,
        'type4': type4, 'type41': type41,
    }
    print(context)
    return render(request, 'df_goods/index.html', context)






