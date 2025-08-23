from django.shortcuts import render, get_object_or_404
from blog.models import Post


def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {
        'posts': posts
        }
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    #  posts = Post.objects.filter(status=1)
    post = get_object_or_404(Post, pk=pid, status=1)
    session_key = f'viewed_post_{post.pk}'
    if not request.session.get(session_key, False):
        post.counted_view += 1
        post.save(update_fields=['counted_view'])
        request.session[session_key] = True
        
    next_post = Post.objects.filter(pk__gt=post.pk).order_by('pk').first()
    prev_post = Post.objects.filter(pk__lt=post.pk).order_by('-pk').first()
    
    
    context = {
        'post': post,
        'next_post': next_post,
        'prev_post': prev_post,
    }
    return render(request, 'blog/blog-single.html', context)


def test(request, pid):
    post = get_object_or_404(Post, pk=pid)
    context = {'post': post}
    return render(request, 'test.html', context)
