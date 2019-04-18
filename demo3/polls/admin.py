from django.contrib import admin
from .models import vote,option
# Register your models here.

class Optioninline(admin.StackedInline):
    model = option
    # 关联个数
    extra = 1

class VoteAdmin(admin.ModelAdmin):
    list_per_page = 2
    list_display = ['votename']
    list_filter = ['votename']
    search_fields = ['votename']

    inlines = [Optioninline]

class OptionAdmin(admin.ModelAdmin):
    list_filter = ['options','voteid',]
    list_display = ['options','number','voteid']
    search_fields = ['options']
    list_per_page = 2


admin.site.register(vote,VoteAdmin)
admin.site.register(option,OptionAdmin)