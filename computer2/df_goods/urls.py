from django.conf.urls import url
from . import views
from .views import *
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^taishiji/$', views.taishiji),
    url(r'^bijiben/$', views.bijiben),
    url(r'^taishiji/list1/$', views.taishijihuoshuo),
    url(r'^taishiji/list2/$', views.taishijilianxaing),
    url(r'^taishiji/list3/$', views.taishijidaier),
    url(r'^taishiji/list4/$', views.taishijipingguo),
    url(r'^taishiji/list1/single/(\d+)/$', views.single),
    url(r'^taishiji/list2/single/(\d+)/$', views.single),
    url(r'^taishiji/list3/single/(\d+)/$', views.single),
    url(r'^taishiji/list4/single/(\d+)/$', views.single),
    url(r'^taishiji/list1/single/(\d+)/gouwuche/(\d+)/$', views.gouwuche),
    # url(r'^list/$', views.list, name='list'),
    # url(r'^list(\d+)_(\d+)_(\d+)/$', views.list, name='list'),      #第一个d+为类型的id, 第二个为当前是第几页,第三个是排序的依据
    # url(r'^(\d+)/$', views.detail, name='detail'),     #详细页
    # url(r'^search/$',MySearchView()),
]