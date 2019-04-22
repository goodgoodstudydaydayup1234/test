from django.db import models
# from tinymce.models import HTMLField

# Create your models here.


class TypeInfo(models.Model):
    ttitle = models.CharField('类型名称', max_length=50)
    isDelete = models.BooleanField('是否删除', default=False)

    def __str__(self):
        return self.ttitle


class GoodsInfo(models.Model):      #商品信息
    gtitle = models.CharField('商品名称', max_length=255)
    gbrand = models.CharField('商品品牌', max_length=50, default='未知')
    gseries = models.CharField('商品系列', max_length=50, null=True, blank=True, default='未知')

    # 商品图片
    gpicb1 = models.ImageField('商品图片', upload_to='static/images', null=True, blank=True)
    gpicb2 = models.ImageField('商品图片', upload_to='static/images', null=True, blank=True)
    gpicb3 = models.ImageField('商品图片', upload_to='static/images', null=True, blank=True)
    gpicb4 = models.ImageField('商品图片', upload_to='static/images', null=True, blank=True)
    gpicb5 = models.ImageField('商品图片', upload_to='static/images', null=True, blank=True)
    gpics1 = models.ImageField('商品图片', upload_to='static/images', null=True, blank=True)
    gpics2 = models.ImageField('商品图片', upload_to='static/images', null=True, blank=True)
    gpics3 = models.ImageField('商品图片', upload_to='static/images', null=True, blank=True)
    gpics4 = models.ImageField('商品图片', upload_to='static/images', null=True, blank=True)
    gpics5 = models.ImageField('商品图片', upload_to='static/images', null=True, blank=True)

    gprice = models.DecimalField('商品价格', max_digits=7, decimal_places=2)        #总共最多有7位,小数占2位
    gclick = models.IntegerField('点击量', default=0)          #商品点击量,便于排人气
    isDelete = models.BooleanField('是否删除', default=False)
    gjianjie = models.CharField('简介', max_length=200, default='暂无')     #商品简介
    gkucun = models.IntegerField('库存', default=500)          #商品库存
    gcontent = models.TextField('详细介绍', default='暂无')                  #商品详细内容
    gtype = models.ForeignKey(TypeInfo, verbose_name='所属分类', on_delete=models.CASCADE)     #商品所属类型

    def __str__(self):
        return self.gtitle



