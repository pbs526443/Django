from django.conf.urls import url

from . import views

app_name = 'booktest'

urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^login/$',views.login,name='login'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^register/$',views.register,name='register'),
    url(r'^user_register/$',views.user_register,name='user_register'),
    url(r'^reader/(\d+)/$',views.reader,name='reader'),
    url(r'^reader_query/(\d+)/$',views.reader_query,name='reader_query'),
    url(r'^reader_info/(\d+)/$',views.reader_info,name='reader_info'),
    url(r'^reader_modify/(\d+)/$',views.reader_modify,name='reader_modify'),
    url(r'^reader_updatemodify/$',views.reader_updatemodify,name='reader_updatemodify'),
    url(r'^reader_book/(\d+)/(\d+)/$',views.reader_book,name='reader_book'),
    url(r'^reader_histroy/(\d+)/$',views.reader_histroy,name='reader_histroy'),
    url(r'^manager/(\d+)/$',views.manager,name='manager'),
    url(r'^manager_login/$',views.manager_login,name='manager_login'),
]