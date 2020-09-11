# 子路由
import django.urls
from firstApp import views

urlpatterns = [
    # path路由匹配
    django.urls.re_path(r'home/', views.home),
    django.urls.re_path(r'^login/', views.login),
    django.urls.re_path(r'quit/', views.quit),
    django.urls.re_path('show_news3/<int:category>/<int:page_no>', views.show_news3),
    # 关键字参数
    django.urls.re_path(r'^show_news2/(?P<category>\d+)/(?P<page_no>\d+)$', views.show_news2),
    # 位置参数
    django.urls.re_path(r'^show_news/(\d+)/(\d+)$', views.show_news),
    django.urls.re_path(r'test', views.test, name='test'),
    django.urls.re_path(r'^student/$', views.student),
    django.urls.re_path(r'^$', views.index, name='index'),  # re_path 可以使正则匹配试图，相当于django版本的url
    # r，表示字符串不转义
    # ... 其他路由
]
