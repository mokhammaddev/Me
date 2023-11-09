# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Contact, Book
# from .forms import ContactForm
#
#
# def index(request):
#     return render(request, 'addition.html')
#
#
# def about(request):
#     return render(request, 'about_me.html')
#
#
# def contact(request):
#     form = ContactForm()
#     if request.method == "POST":
#         form = ContactForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     ctx = {
#         'form': form,
#     }
#     return render(request, "contact.html", ctx)
#
#
# def feedback(request):
#     feedbacks = Contact.objects.order_by('-id')
#     ctx = {
#         'feedbacks': feedbacks
#     }
#     return render(request, 'feedback.html', ctx)
#
#
# def book(request):
#     books = Book.objects.order_by('-id')
#     ctx = {
#         'books': books,
#     }
#     return render(request, 'book.html', ctx)
#
#
# def book_detail(request, pk):
#     books = get_object_or_404(Book, id=pk)
#     ctx = {
#         'book': books
#     }
#     return render(request, 'book_detail.html')
