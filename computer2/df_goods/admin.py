from django.contrib import admin
from .models import TypeInfo, GoodsInfo
# Register your models here.


class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'ttitle']
    list_filter = ['ttitle']
    search_fields = ['ttitle']
    list_per_page = 10


class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'gtitle', 'gbrand', 'gseries', 'gprice', 'gkucun', 'gclick', 'gtype', 'gpicb1']
    list_filter = ['gbrand']
    search_fields = ['gbrand']
    list_per_page = 10


admin.site.register(TypeInfo, TypeInfoAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)

