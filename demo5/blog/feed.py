from django.contrib.syndication.views import Feed
from .models import article
from django.shortcuts import reverse

class ArticleFeed(Feed):
    '''
    进行网站包装成XML格式
    # RSS 可以把网站包装成XML格式
    # 可以通过RSS聚合工具订阅，该工具会获取RSS订阅更新的内容
    # 不用每次进入博客查看更新
    '''

    title = "文章"
    description = "摘要"
    link = "/"

    def items(self):
        return article.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    def item_link(self, item):
        return reverse('blog:single',args=(item.id,))