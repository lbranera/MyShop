import math
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
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
        data = {'book': book, 'comments':comments, 'overall_rating': round(overall_rating,2), "rating_floor": math.floor(overall_rating), 'rating_float': not overall_rating.is_integer()}
    else: 
        data = {'book': book } 
    
    form = ShoppingCartForm({"user": request.user.id, "book": book.id, "quantity": 1})
    data["form"] = form

    if( request.method == "POST"):
        form = ShoppingCartForm(request.POST)
        if( form.is_valid() ):
            form.save()
            return redirect("/")
            
    return render(request, 'products/book.html', data)


def register(request):
    form = UserForm()

    '''
    if( request.method == "POST"):
        form = UserForm(request.POST)
        if( form.is_valid() ):
            new_object = form.save(commit=False)
            new_object.password = make_password(form.cleaned_data['password'])
            new_object.save()
            return redirect('/')
    '''

    if( request.method == "POST"):
        form = UserForm(request.POST)
        if( form.is_valid() ):
            form.save()
            messages.success(request, "Account was created for "+form.cleaned_data.get("username"))
            return redirect('/login')

    data = {"form": form}
    return render(request, 'products/register.html', data)

def login_page(request):
    if( request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            print("Login Success.")
            return redirect('/')
        else:
            print("Login Fail.")
            messages.error(request, "Incorrect password or username.")

        '''
        try:
            user = User.objects.get(username=username)
            if ( check_password(password, user.password) ):
                print("Login success.")
                
            return redirect('/')

        except User.DoesNotExist:
            return redirect('login')
        '''

    return render(request, 'products/login.html')


def logout_page(request):
    logout(request)
    return redirect('login')