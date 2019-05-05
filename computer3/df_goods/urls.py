from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^list/$', views.list),

    url(r'^$', views.index),
    url(r'^singlec/(\d+)/$', views.singlei),
    url(r'^taishiji/$', views.taishiji),
    url(r'^bijiben/$', views.bijiben),

    url(r'^taishiji/list1/$', views.taishiji_huashuo),
    url(r'^taishiji/list2/$', views.taishiji_lianxiang),
    url(r'^taishiji/list3/$', views.taishiji_daier),
    url(r'^taishiji/list4/$', views.taishiji_pingguo),
    url(r'^taishiji/list4/single/(\d+)/$', views.single),
    url(r'^taishiji/list3/single/(\d+)/$', views.single),
    url(r'^taishiji/list2/single/(\d+)/$', views.single),
    url(r'^taishiji/list1/single/(\d+)/$', views.single),
    url(r'^taishiji/single/(\d+)/$', views.single),

    url(r'^bijiben/list11/$', views.bijiben_huashuo),
    url(r'^bijiben/list22/$', views.bijiben_lianxiang),
    url(r'^bijiben/list33/$', views.bijiben_daier),
    url(r'^bijiben/list44/$', views.bijiben_pingguo),
    url(r'^bijiben/list44/single1/(\d+)/$', views.single1),
    url(r'^bijiben/list33/single1/(\d+)/$', views.single1),
    url(r'^bijiben/list22/single1/(\d+)/$', views.single1),
    url(r'^bijiben/list11/single1/(\d+)/$', views.single1),
    url(r'^bijiben/single1/(\d+)/$', views.single1),

    url(r'^cpu/$', views.cpu),
    url(r'^cpu/singlec/(\d+)/$', views.singlec),

    url(r'^zhuban/$', views.zhuban),
    url(r'^zhuban/singlez/(\d+)/$', views.singlez),

    url(r'^xianka/$', views.xianka),
    url(r'^xianka/singlex/(\d+)/$', views.singlex),

    url(r'^yingpan/$', views.yingpan),
    url(r'^yingpan/singley/(\d+)/$', views.singley),

    url(r'^jixiang/$', views.jixiang),
    url(r'^jixiang/singlej/(\d+)/$', views.singlej),

]