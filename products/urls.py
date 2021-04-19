from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('book/<str:pk>/', views.book, name="book"),
    path('register/', views.register, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
]
