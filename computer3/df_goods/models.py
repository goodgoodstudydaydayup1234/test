from django.db import models

# Create your models here.


class Type(models.Model):
    name = models.CharField('类型', max_length=255)
    isDelete = models.BooleanField('是否删除', default=False)

    def __str__(self):
        return self.name


class Taishiji(models.Model):
    tname = models.CharField('名称', max_length=255)
    tbrand = models.CharField('品牌', max_length=50, default='未知')
    tseries = models.CharField('系列', max_length=50, null=True, blank=True, default='未知')
    tprice = models.DecimalField('价格', max_digits=7, decimal_places=2)  # 总共最多有7位,小数占2位
    tcpu = models.CharField('CPU', max_length=20)
    tdisplay_card = models.CharField('显卡', max_length=20)
    tsize = models.CharField('尺寸', max_length=20)
    tos = models.CharField('操作系统', max_length=50)
    tneicun = models.CharField('内存', max_length=50)
    tclick = models.IntegerField('点击量', default=0)  # 商品点击量,便于排人气
    isDelete = models.BooleanField('是否删除', default=False)
    tjianjie = models.CharField('简介', max_length=200, default='暂无')  # 商品简介
    tkucun = models.IntegerField('库存', default=500)  # 商品库存

    # 商品图片
    timgb1 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    timgb2 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    timgb3 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    timgb4 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    timgb5 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    timgs1 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    timgs2 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    timgs3 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    timgs4 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    timgs5 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)

    def __str__(self):
        return self.tname


class Bijiben(models.Model):
    bname = models.CharField('名称', max_length=255)
    bbrand = models.CharField('品牌', max_length=20)
    bcolor = models.CharField('颜色', max_length=20)
    bsize = models.CharField('尺寸', max_length=50)
    bcpu = models.CharField('CPU', max_length=20)
    bprice = models.DecimalField('价格', max_digits=7, decimal_places=2)
    bweight = models.CharField('重量', max_length=20)
    bcpu_speed = models.CharField('CPU速度', max_length=100)
    bneicun = models.CharField('内存', max_length=100)
    bhard_disk = models.CharField('硬盘', max_length=100)
    bdisplay_card = models.CharField('显卡', max_length=50)
    bos = models.CharField('操作系统', max_length=50)
    baverage_standby = models.CharField('待机时间', max_length=50)
    bclick = models.IntegerField('点击量', default=0)  # 商品点击量,便于排人气
    isDelete = models.BooleanField('是否删除', default=False)
    bjianjie = models.CharField('简介', max_length=200, default='暂无')  # 商品简介
    bkucun = models.IntegerField('库存', default=500)  # 商品库存

    # 商品图片
    bimgb1 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    bimgb2 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    bimgb3 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    bimgb4 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    bimgb5 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    bimgs1 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    bimgs2 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    bimgs3 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    bimgs4 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    bimgs5 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)

    def __str__(self):
        return self.bname


class Cpu(models.Model):
    cname = models.CharField('名称', max_length=255)
    cprice = models.DecimalField('价格', max_digits=7, decimal_places=2)
    cbrand = models.CharField('品牌', max_length=50)
    cseries = models.CharField('系列', max_length=50)
    ccore_num = models.CharField('核心数量', max_length=20)
    cmodel = models.CharField('型号', max_length=50)
    cclick = models.IntegerField('点击量', default=0)  # 商品点击量,便于排人气
    isDelete = models.BooleanField('是否删除', default=False)
    cjianjie = models.CharField('简介', max_length=200, default='暂无')  # 商品简介
    ckucun = models.IntegerField('库存', default=500)  # 商品库存

    # 商品图片
    cimgb1 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    cimgb2 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    cimgb3 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    cimgb4 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    cimgb5 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    cimgs1 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    cimgs2 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    cimgs3 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    cimgs4 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    cimgs5 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)

    def __str__(self):
        return self.cname


class Zhuban(models.Model):
    zname = models.CharField('名称', max_length=255)
    zbrand = models.CharField('品牌', max_length=50)
    zmodel = models.CharField('型号', max_length=50)
    zcpu = models.CharField('CPU', max_length=50)
    zweight = models.CharField('重量', max_length=50)
    zinterface = models.CharField('接口', max_length=50)
    zclick = models.IntegerField('点击量', default=0)  # 商品点击量,便于排人气
    isDelete = models.BooleanField('是否删除', default=False)
    zjianjie = models.CharField('简介', max_length=200, default='暂无')  # 商品简介
    zkucun = models.IntegerField('库存', default=500)  # 商品库存
    zprice = models.DecimalField('价格', max_digits=7, decimal_places=2)

    # 商品图片
    zimgb1 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    zimgb2 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    zimgb3 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    zimgb4 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    zimgb5 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    zimgs1 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    zimgs2 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    zimgs3 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    zimgs4 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    zimgs5 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)

    def __str__(self):
        return self.zname


class Xianka(models.Model):
    xname = models.CharField('名称', max_length=255)
    xbrand = models.CharField('品牌', max_length=50)
    xmodel = models.CharField('型号', max_length=50)
    xinterface_type = models.CharField('接口类型', max_length=50)
    xcore_brand = models.CharField('核心品牌', max_length=100)
    xcore_model = models.CharField('核心型号', max_length=100)
    xneicun_type = models.CharField('内存类型', max_length=50)
    xneicun = models.CharField('内存', max_length=50)
    xprice = models.DecimalField('价格', max_digits=7, decimal_places=2)
    xclick = models.IntegerField('点击量', default=0)  # 商品点击量,便于排人气
    isDelete = models.BooleanField('是否删除', default=False)
    xjianjie = models.CharField('简介', max_length=200, default='暂无')  # 商品简介
    xkucun = models.IntegerField('库存', default=500)  # 商品库存

    # 商品图片
    ximgb1 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    ximgb2 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    ximgb3 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    ximgb4 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    ximgb5 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    ximgs1 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    ximgs2 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    ximgs3 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    ximgs4 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    ximgs5 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)

    def __str__(self):
        return self.xname


class Yingpan(models.Model):
    yname = models.CharField('名称', max_length=255)
    ybrand = models.CharField('品牌', max_length=50)
    ymodel = models.CharField('型号', max_length=50)
    ytype = models.CharField('类型', max_length=50)
    ycapacity = models.CharField('容量', max_length=50)
    ysize = models.CharField('尺寸', max_length=50)
    yprice = models.DecimalField('价格', max_digits=7, decimal_places=2)
    ycolor = models.CharField('颜色', max_length=20)
    yos = models.CharField('操作系统', max_length=50)
    yweight = models.CharField('重量', max_length=50)
    youtputinterface = models.CharField('输出接口', max_length=20)
    yclick = models.IntegerField('点击量', default=0)  # 商品点击量,便于排人气
    isDelete = models.BooleanField('是否删除', default=False)
    yjianjie = models.CharField('简介', max_length=200, default='暂无')  # 商品简介
    ykucun = models.IntegerField('库存', default=500)  # 商品库存

    # 商品图片
    yimgb1 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    yimgb2 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    yimgb3 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    yimgb4 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    yimgb5 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    yimgs1 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    yimgs2 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    yimgs3 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    yimgs4 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    yimgs5 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)

    def __str__(self):
        return self.yname


class Jixiang(models.Model):
    jname = models.CharField('名称', max_length=255)
    jbrand = models.CharField('品牌', max_length=50)
    jweight = models.CharField('重量', max_length=50)
    jsize = models.CharField('尺寸', max_length=100)
    jprice = models.DecimalField('价格', max_digits=7, decimal_places=2)
    jclick = models.IntegerField('点击量', default=0)  # 商品点击量,便于排人气
    isDelete = models.BooleanField('是否删除', default=False)
    jjianjie = models.CharField('简介', max_length=200, default='暂无')  # 商品简介
    jkucun = models.IntegerField('库存', default=500)  # 商品库存

    # 商品图片
    jimgb1 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    jimgb2 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    jimgb3 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    jimgb4 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    jimgb5 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    jimgs1 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    jimgs2 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    jimgs3 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    jimgs4 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    jimgs5 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)

    def __str__(self):
        return self.jname


class Yjxsq(models.Model):
    qname = models.CharField('名称', max_length=255)
    qbrand = models.CharField('品牌', max_length=50)
    qmodel = models.CharField('型号', max_length=100)
    qcolor = models.CharField('颜色', max_length=50)
    qweight = models.CharField('重量', max_length=50)
    qsize = models.CharField('尺寸', max_length=50)
    qresoluation = models.CharField('分辨率', max_length=50)
    qaspect_ratio = models.CharField('屏幕宽高比', max_length=50)
    qprice = models.DecimalField('价格', max_digits=7, decimal_places=2)
    qclick = models.IntegerField('点击量', default=0)  # 商品点击量,便于排人气
    isDelete = models.BooleanField('是否删除', default=False)
    qjianjie = models.CharField('简介', max_length=200, default='暂无')  # 商品简介
    qkucun = models.IntegerField('库存', default=500)  # 商品库存

    # 商品图片
    qimgb1 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    qimgb2 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    qimgb3 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    qimgb4 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    qimgb5 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    qimgs1 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    qimgs2 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    qimgs3 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    qimgs4 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    qimgs5 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)

    def __str__(self):
        return self.qname


class Yinxiang(models.Model):
    xname = models.CharField('名称', max_length=255)
    xbrand = models.CharField('品牌', max_length=50)
    xmodel = models.CharField('型号', max_length=50)
    xtype = models.CharField('类型', max_length=50)
    xcolor = models.CharField('颜色', max_length=50)
    xpower_supply_way = models.CharField('供电方式', max_length=50)
    xprice = models.DecimalField('价格', max_digits=7, decimal_places=2)
    xclick = models.IntegerField('点击量', default=0)  # 商品点击量,便于排人气
    isDelete = models.BooleanField('是否删除', default=False)
    xjianjie = models.CharField('简介', max_length=200, default='暂无')  # 商品简介
    xkucun = models.IntegerField('库存', default=500)  # 商品库存

    # 商品图片
    ximgb1 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    ximgb2 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    ximgb3 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    ximgb4 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    ximgb5 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    ximgs1 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    ximgs2 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    ximgs3 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    ximgs4 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    ximgs5 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)

    def __str__(self):
        return self.xname


class Shubiao(models.Model):
    sname = models.CharField('名称', max_length=255)
    sbrand = models.CharField('品牌', max_length=50)
    smodel = models.CharField('型号', max_length=50)
    stype = models.CharField('类型', max_length=50)
    sconnet_way = models.CharField('连接方式', max_length=50)
    sprice = models.DecimalField('价格', max_digits=7, decimal_places=2)
    sclick = models.IntegerField('点击量', default=0)  # 商品点击量,便于排人气
    isDelete = models.BooleanField('是否删除', default=False)
    sjianjie = models.CharField('简介', max_length=200, default='暂无')  # 商品简介
    skucun = models.IntegerField('库存', default=500)  # 商品库存

    # 商品图片
    simgb1 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    simgb2 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    simgb3 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    simgb4 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    simgb5 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    simgs1 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    simgs2 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    simgs3 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    simgs4 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    simgs5 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)

    def __str__(self):
        return self.sname


class Jianpan(models.Model):
    pname = models.CharField('名称', max_length=255)
    pbrand = models.CharField('品牌', max_length=50)
    pmodel = models.CharField('型号', max_length=50)
    pconnect_way = models.CharField('连接方式', max_length=50)
    pprice = models.DecimalField('价格', max_digits=7, decimal_places=2)
    pweight = models.CharField('重量', max_length=50)
    pcolor = models.CharField('颜色', max_length=50)
    pbacklighting = models.CharField('背光', max_length=50)
    pclick = models.IntegerField('点击量', default=0)  # 商品点击量,便于排人气
    isDelete = models.BooleanField('是否删除', default=False)
    pjianjie = models.CharField('简介', max_length=200, default='暂无')  # 商品简介
    pkucun = models.IntegerField('库存', default=500)  # 商品库存

    # 商品图片
    pimgb1 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    pimgb2 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    pimgb3 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    pimgb4 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    pimgb5 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    pimgs1 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    pimgs2 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    pimgs3 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    pimgs4 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    pimgs5 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)

    def __str__(self):
        return self.pname


class Neicun(models.Model):
    nname = models.CharField('名称', max_length=255)
    nbrand = models.CharField('品牌', max_length=50)
    ncapacity = models.CharField('内存', max_length=50)
    nmodel = models.CharField('型号', max_length=50)
    ntype = models.CharField('类型', max_length=50)
    nspeed = models.CharField('速度', max_length=50)
    napplicable = models.CharField('适应机型', max_length=50)
    nprice = models.DecimalField('价格', max_digits=7, decimal_places=2)
    nclick = models.IntegerField('点击量', default=0)  # 商品点击量,便于排人气
    isDelete = models.BooleanField('是否删除', default=False)
    njianjie = models.CharField('简介', max_length=200, default='暂无')  # 商品简介
    nkucun = models.IntegerField('库存', default=500)  # 商品库存

    # 商品图片
    nimgb1 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    nimgb2 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    nimgb3 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    nimgb4 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    nimgb5 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    nimgs1 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    nimgs2 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    nimgs3 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    nimgs4 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)
    nimgs5 = models.ImageField('图片', upload_to='static/images', null=True, blank=True)

    def __str__(self):
        return self.nname







