from django.contrib import admin
from .models import BookInfo,HeroInfo
# Register your models here.

class HeroInfoinline(admin.StackedInline):
    # 与HeroInfo相连
    model = HeroInfo
    # 关联个数
    extra = 1

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['title','pub_date',]
    list_filter = ['btitle',]
    search_fields = ['btitle',]
    list_per_page = 2

    # 在添加书籍的时候可以额外添加英雄
    inlines = [HeroInfoinline]

admin.site.register(BookInfo,BookInfoAdmin)


class HeroInfoAdmin(admin.ModelAdmin):
    # 显示字段，可以点击列头进行排序
    list_display = ['name','gender','content',]
    # 过滤字段，过滤框会出现在右侧
    list_filter = ['hname','hgender',]
    # 搜索字段，搜索框会出现在上方
    search_fields = ['hname','hcontent',]
    # 分页，分页框会出现在下侧
    list_per_page = 2

admin.site.register(HeroInfo,HeroInfoAdmin)

'''
通过少量代码实现强大的后台管理
需要将特定的数据模型注册  才能在后台管理
'''