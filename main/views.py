from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm


def index(request):
    return render(request, 'addition.html')


def about(request):
    return render(request, 'about_me.html')


def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(data=request.POST) or ContactForm(data=request.FILES)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # avatar = form.cleaned_data['avatar']
            # email = form.cleaned_data['email']
            # phone_number = form.cleaned_data['phone_number']
            # message = form.cleaned_data['message']
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
