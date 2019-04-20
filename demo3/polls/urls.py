from django.conf.urls import url
from . import views

app_name = 'polls'

urlpatterns = [
    url(r'^$',views.votelist,name='list'),
    url(r'^optionlist/(\d+)/$',views.optionlist,name='optionlist'),
    url(r'^votedetail/$',views.votedetail,name='votedetail'),
    # url(r'^optdetail/(\d+)/$',views.optdetail,name='optdetail'),
    url(r'^addvote/$',views.addvote,name='addvote'),
    url(r'^voteadd/$',views.voteadd,name='voteadd'),
    url(r'^updatevote/(\d+)/$',views.updatevote,name='updatevote'),
    url(r'^voteupdate/$',views.voteupdate,name='voteupdate'),
    url(r'^votdelete/(\d+)/$',views.votdelete,name='votdelete'),
    url(r'^addoption/(\d+)/$',views.addoption,name='addoption'),
    url(r'^optionadd/$',views.optionadd,name='optionadd'),
    url(r'^updateoption/(\d+)/$',views.updateoption,name='updateoption'),
    url(r'^optionupdate/$',views.optionupdate,name='optionupdate'),
    url(r'^deleteoption/(\d+)/$',views.deleteoption,name='deleteoption'),
    url(r'^optdetail/(\d+)/$',views.optdetail,name='optdetail'),
]