from django import template
from ..models import article,tag,comment,cation
# 得到Django负责管理标签和过滤器的类
register = template.Library()

@register.simple_tag
def getarticle(num=3):
    '''
    获取最新文章，默认显示3篇
    :param num:
    :return:
    '''
    return article.objects.order_by("-time_creation")[:num]

@register.simple_tag
def getdatelist(num=3):
    '''
    返回最近月份
    :param num:
    :return:
    '''
    return  article.objects.dates("time_creation", "month", order="DESC")[:num]

@register.simple_tag
def getcategorys():
    '''
    返回分类
    :return:
    '''
    return cation.objects.all()

@register.simple_tag
def gettags():
    '''
    返回标签云
    :return:
    '''
    return tag.objects.all()