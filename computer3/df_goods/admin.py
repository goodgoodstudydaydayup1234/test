from django.contrib import admin
from .models import Type, Taishiji, Bijiben, Zhuban, Xianka, Cpu, Neicun, Yingpan, Jixiang, Yjxsq, Yinxiang, Shubiao, Jianpan
# Register your models here.


class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_per_page = 10
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(Type, TypeAdmin)


class TaishijiAdmin(admin.ModelAdmin):
    list_display = ['id', 'tname', 'tbrand', 'tseries', 'tprice', 'tcpu', 'tdisplay_card', 'tsize', 'tos', 'tneicun', 'tclick', 'isDelete', 'tjianjie', 'tkucun']
    list_per_page = 10
    list_filter = ['tbrand', 'tcpu']
    search_fields = ['tbrand', 'tcpu']


admin.site.register(Taishiji, TaishijiAdmin)


class BijibenAdmin(admin.ModelAdmin):
    list_display = ['id', 'bname', 'bbrand', 'bcolor', 'bsize', 'bcpu', 'bprice', 'bweight', 'bcpu_speed', 'bneicun', 'bhard_disk', 'isDelete', 'bjianjie', 'bkucun']
    list_per_page = 10
    list_filter = ['bbrand']
    search_fields = ['bbrand']


admin.site.register(Bijiben, BijibenAdmin)


class ZhubanAdmin(admin.ModelAdmin):
    list_display = ['id', 'zname', 'zbrand', 'zmodel', 'zcpu', 'zweight', 'zinterface', 'zclick', 'isDelete', 'zjianjie', 'zkucun', 'zprice']
    list_per_page = 10
    list_filter = ['zbrand']
    search_fields = ['zbrand']


admin.site.register(Zhuban, ZhubanAdmin)


class XiankaAdmin(admin.ModelAdmin):
    list_display = ['id', 'xname', 'xbrand', 'xmodel', 'xinterface_type', 'xcore_brand', 'xcore_model', 'xneicun_type', 'xneicun', 'xprice']
    list_per_page = 10
    list_filter = ['xbrand']
    search_fields = ['xbrand']


admin.site.register(Xianka, XiankaAdmin)


class CpuAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'cprice', 'cbrand', 'cseries', 'ccore_num', 'cmodel', 'ckucun']
    list_per_page = 10
    list_filter = ['cbrand']
    search_fields = ['cbrand']


admin.site.register(Cpu, CpuAdmin)


class NeicunAdmin(admin.ModelAdmin):
    list_display = ['id', 'nname', 'nbrand', 'ncapacity', 'nmodel', 'ntype', 'nspeed', 'napplicable', 'nprice', 'nkucun']
    list_per_page = 10
    list_filter = ['nbrand']
    search_fields = ['nbrand']


admin.site.register(Neicun, NeicunAdmin)


class YingpanAdmin(admin.ModelAdmin):
    list_display = ['id', 'yname', 'ybrand', 'ymodel', 'ytype', 'ycapacity', 'ysize', 'yprice', 'ykucun']
    list_per_page = 10
    list_filter = ['ybrand']
    search_fields = ['ybrand']


admin.site.register(Yingpan, YingpanAdmin)


class JixiangAdmin(admin.ModelAdmin):
    list_display = ['id', 'jname', 'jbrand', 'jweight', 'jsize', 'jprice', 'jclick', 'jkucun']
    list_per_page = 10
    list_filter = ['jbrand']
    search_fields = ['jbrand']


admin.site.register(Jixiang, JixiangAdmin)


class YjxsqAdmin(admin.ModelAdmin):
    list_display = ['id', 'qname', 'qbrand', 'qmodel', 'qcolor', 'qprice', 'qkucun']
    list_per_page = 10
    list_filter = ['qbrand']
    search_fields = ['qbrand']


admin.site.register(Yjxsq, YjxsqAdmin)


class YinxiangAdmin(admin.ModelAdmin):
    list_display = ['id', 'xname', 'xbrand', 'xmodel', 'xtype', 'xprice', 'xkucun']
    list_per_page = 10
    list_filter = ['xbrand']
    search_fields = ['xbrand']


admin.site.register(Yinxiang, YinxiangAdmin)


class ShubiaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'sname', 'sbrand', 'smodel', 'stype', 'sprice', 'skucun']
    list_per_page = 10
    list_filter = ['sbrand']
    search_fields = ['sbrand']


admin.site.register(Shubiao, ShubiaoAdmin)


class JianpanAdmin(admin.ModelAdmin):
    list_display = ['id', 'pname', 'pbrand', 'pmodel', 'pconnect_way', 'pprice', 'pkucun']
    list_per_page = 10
    list_filter = ['pbrand']
    search_fields = ['pbrand']


admin.site.register(Jianpan, JianpanAdmin)

