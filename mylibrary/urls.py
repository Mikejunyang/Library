from django.urls import path
from . import views

urlpatterns = [
    path("", views.bookTable, name = "book"),
    path("bookinstance/<int:id>/", views.details, name = "bookinstance"),
    path("author/", views.author, name = "author"),
]