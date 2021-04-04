from django.shortcuts import render
from django.http import HttpResponse
from products.models import Book
# Create your views here.

def home(request):
    books = Book.objects.all()
    data = {'books': books}
    return render(request, 'products/home.html', data)

def book(request,pk):
    book = Book.objects.get(id=pk)
    data = {'book': book}
    return render(request, 'products/book.html', data)


def register(request):
    return render(request, 'products/register.html')

def login(request):
    return render(request, 'products/login.html')