from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^index_action/(\d+)/$',views.index_action,name='index_action'),
    url(r'^index_tag/(\d+)/$',views.index_tag,name='index_tag'),
    url(r'^index_time/(\d+)/(\d+)/$',views.index_time,name='index_time'),
    url(r'^single_hr/(\d+)/$',views.single_hr,name='single_hr'),
    url(r'^single/(\d+)/$',views.single,name='single'),
    url(r'^addcomm/$', views.addcomm, name='addcomm'),
]