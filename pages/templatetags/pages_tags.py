from django import template
from blog.models import Post

register = template.Library()

@register.inclusion_tag('pages/pages_latest_posts.html')
def latest_posts(count=6):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:count]
    return {'posts': posts}