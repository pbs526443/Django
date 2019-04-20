from django.conf.urls import url
from . import views

app_name = 'booktest'

urlpatterns = [
    url(r'^$', views.index,name='index'),
    # url('index/',views.index),
    url(r'^list/',views.list,name='list'),
    # url(r'index/$',views.index),
    # url(r'detail/(\d+)/(\d+)/$',views.detail),
    url(r'^details/(\d+)/$',views.details,name='details'),
    url(r'^delete/(\d+)/$',views.delete,name='delete'),
    # url(r'^bookadd/(\d+)/$',views.bookadd,name='bookadd'),
    url(r'^heroadd/(\d+)/$',views.heroadd,name='heroadd'),
    url(r'^heroinfoadd/$',views.heroinfoadd,name='heroinfoadd'),
    url(r'^bookadd/$',views.bookadd,name='bookadd'),
    url(r'^addbook/$',views.addbook,name='addbook'),
    url(r'^bookupdate/(\d+)/$',views.bookupdate,name='bookupdate'),
    url(r'^updatebook/$',views.updatebook,name='updatebook'),
    url(r'^herodelete/(\d+)/$',views.herodelete,name='herodelete'),
    url(r'^heroupdate/(\d+)/$',views.heroupdate,name='heroupdate'),
    url(r'^addheroinfo/$',views.addheroinfo,name='addheroinfo'),
]