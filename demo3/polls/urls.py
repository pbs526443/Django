from django.conf.urls import url
from . import views

app_name = 'polls'

urlpatterns = [
    url(r'^$',views.votelist,name='list'),
    url(r'^optionlist/(\d+)/$',views.optionlist,name='optionlist'),
    url(r'^votedetail/$',views.votedetail,name='votedetail'),
]