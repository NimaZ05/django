from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NameForm, ContactForm, NewsletterForm
from django.contrib import messages


def home_view(request):
    return render(request, 'pages/index.html')


def about_view(request):
    return render(request, 'pages/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'your ticket submited successfully')
        else:
            messages.add_message(request, messages.ERROR,
                                 'your ticket didnt submited ')

    form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form})


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'your ticket submited successfully')
        else:
            messages.add_message(request, messages.ERROR,
                                 'your ticket didnt submited ')
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
