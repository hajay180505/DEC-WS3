from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("book-ticket/", views.book_ticket, name="book-ticket"),
    path('book/<int:id>/', views.book, name='book'),
]
