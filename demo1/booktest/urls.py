from django.conf.urls import url
from . import views
urlpatterns = [
    # url('index/',views.index),
    url(r'list/',views.list),
    url(r'index/$',views.index),
    url(r'detail/(\d+)/(\d+)/$',views.detail),
    url(r'details/(\d+)/$',views.details),
]