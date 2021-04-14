import math
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from products.models import *
from products.forms import *

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
    form = UserForm()

    if( request.method == "POST"):
        form = UserForm(request.POST)
        if( form.is_valid() ):
            new_object = form.save(commit=False)
            new_object.password = make_password(form.cleaned_data['password'])
            new_object.save()

            form.save()
            return redirect('/')

    data = {"form": form}
    return render(request, 'products/register.html', data)

def login(request):
    return render(request, 'products/login.html')