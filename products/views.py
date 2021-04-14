import math
from django.shortcuts import render
from django.http import HttpResponse
from products.models import *
# Create your views here.

def home(request):
    books = Book.objects.all()
    data = {'books': books}
    return render(request, 'products/home.html', data)

def book(request,pk):
    book = Book.objects.get(id=pk)
    comments = book.comment_set.all()

    if ( len(comments) != 0 ):

        overall_rating = 0
        for comment in comments:
            overall_rating += comment.rating 
    
        overall_rating = overall_rating/len(comments)

        data = {'book': book, 'with_comments': True, 'comments':comments, 'overall_rating': round(overall_rating,2), "rating_floor": math.floor(overall_rating), 'rating_float': not overall_rating.is_integer()}
    
    else: 

        data = {'book': book, 'with_comments': False} 

    return render(request, 'products/book.html', data)


def register(request):
    return render(request, 'products/register.html')

def login(request):
    return render(request, 'products/login.html')