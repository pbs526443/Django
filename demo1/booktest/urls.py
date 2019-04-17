from django.conf.urls import url
from . import views

app_name = 'booktest'

urlpatterns = [
    url(r'^$', views.index,name='index'),
    # url('index/',views.index),
    url(r'^booklist/',views.list,name='list'),
    # url(r'index/$',views.index),
    # url(r'detail/(\d+)/(\d+)/$',views.detail),
    url(r'^bookdetails/(\d+)/$',views.details,name='details'),
]