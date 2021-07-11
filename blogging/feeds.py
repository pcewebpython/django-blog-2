from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post

class LatestEntriesFeed(Feed):
    title = 'Most Recent Posts'
    link = '/sitenews/'
    description = '5 Most Recent Posts to Site'

    def items(self):
        return Post.objects.order_by('-published_date')[:5]

    def item_title(self, item):
        return item.title

    def item_author(self, item):
        return item.author

    def item_link(self, item):
        return reverse('post', args=[item.pk])
