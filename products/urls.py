from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('book/<str:pk>/', views.book, name="book"),
    
    path('cart/', views.cart, name="cart"),
    path('add-cart/', views.add_cart, name="add_cart"),
    path('update-cart/<str:pk>/', views.update_cart, name="update_cart"),
    path('delete-cart/<str:pk>/', views.delete_cart, name="delete_cart"),

    path('register/', views.register, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
]
