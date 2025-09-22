from django import template
from blog.models import Post

register = template.Library()

@register.inclusion_tag('pages/pages_latest_posts.html')
def latest_posts(count=6):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:count]
    return {'posts': posts}


@register.inclusion_tag('pages/latest_posts_widget.html')
def show_latest_posts(count=8):
    latest_posts = Post.objects.order_by('-created_date')[:count]
    return {'latest_posts': latest_posts}