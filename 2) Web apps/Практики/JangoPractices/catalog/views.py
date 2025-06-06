from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Book
from .forms import BookForm, RegisterForm
from django.contrib.auth import login
def book_list(request):
    books = Book.objects.all().order_by('id')

    q = request.GET.get('q', '')
    auth = request.GET.get('author', '')
    genre = request.GET.get('genre', '')

    if q:
        books = books.filter(title__icontains=q)
    if auth:
        books = books.filter(author__first_name__icontains=auth) | books.filter(author__last_name__icontains=auth)
    if genre:
        books = books.filter(genre__name__icontains=genre)

    paginator = Paginator(books, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'catalog/index.html', {
        'page_obj': page_obj,
        'q': q,
        'author': auth,
        'genre': genre
    })

@login_required
def add_book(request):
    form = BookForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Книгу успішно додано!')
        return redirect('book_list')
    return render(request, 'catalog/add_book.html', {"form": form})

@login_required
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Книгу успішно відредаговано!')
        return redirect('book_list')
    return render(request, 'catalog/edit_book.html', {"form": form})

@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Книгу успішно видалено!')
        return redirect('book_list')
    return render(request, 'catalog/delete_book.html', {"book": book})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request,'Реєстрація успішна!')
            return redirect('book_list')
    else:
        form = RegisterForm()

    return render(request,'catalog/register.html',{'form':form})