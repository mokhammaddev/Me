from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm


def index(request):
    return render(request, 'addition.html')


def about(request):
    return render(request, 'about_me.html')


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('/')

    ctx = {
        'form': form,
    }
    return render(request, "contact.html", ctx)


def feedback(request):
    feedbacks = Contact.objects.order_by('-id')
    ctx = {
        'feedbacks': feedbacks
    }
    return render(request, 'feedback.html', ctx)
