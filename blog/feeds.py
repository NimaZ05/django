from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post


class LatestEntriesFeed(Feed):
    title = "blog newest posts"
    link = "/rss/feed"
    description = "best blog posts"

    def items(self):
        post = Post.objects.filter(status=True)
        return post

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:50]
