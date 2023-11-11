from django.shortcuts import render, redirect, get_object_or_404
# from .models import Contact, Book
from .forms import ContactForm


def index(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('/')
    ctx = {
        'contact_form': contact_form,
    }
    return render(request, 'index.html', ctx)
