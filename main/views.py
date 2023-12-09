from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm


def index(request):
    contacts = Contact.objects.order_by('-id')
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        print("Contact Form -->", contact_form)
        if contact_form.is_valid():
            print("Kirdi")
            contact_form.save()
            return redirect('index')
    print("Kirmadi")

    ctx = {
        'contact_form': contact_form,
        'contacts': contacts,
    }
    return render(request, 'index.html', ctx)
