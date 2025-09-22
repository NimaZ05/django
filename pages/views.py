from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm, NewsletterForm
from django.contrib import messages
from blog.models import Post


def home_view(request):
    latest_posts = Post.objects.order_by('-created_date')[:8]
    context = {'latest_posts':latest_posts}
    return render(request, 'pages/index.html', context)


def about_view(request):
    return render(request, 'pages/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'your ticket submited successfully')
        else:
            messages.error(request, 'your ticket didnt submited ')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'pages/contact.html', context)


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'your ticket submited successfully')
        else:
            messages.error(request, 'your ticket didnt submited ')
        return HttpResponseRedirect("/")


def test(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Done")
    else:
        form = ContactForm()
    return render(request, 'test.html', {'form': form})
