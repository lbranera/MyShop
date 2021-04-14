from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=100, null=True)
    price = models.FloatField()
    description = models.CharField(max_length=500, null=True)
    weight = models.FloatField(null=True)
    dimensions = models.CharField(max_length=50, null=True)
    edition = models.CharField(max_length=50, null=True)
    language = models.CharField(max_length=50, null=True)
    pages = models.IntegerField(null=True)
    subtitle = models.CharField(max_length=500, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

class User(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=100, null=True) 
    email = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name+" "+self.last_name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100, null=True)
    rating = models.IntegerField(
        null=True,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )
    date_created = models.DateTimeField(auto_now_add=True, null=True)

