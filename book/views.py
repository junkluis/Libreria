# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from book.models import Book
from book.forms import BookForm


class BookList(ListView):
    model = Book


class BookView(DetailView):
    model = Book


class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    
    success_url = reverse_lazy('book_list')


class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    
    success_url = reverse_lazy('book_list')


class BookDelete(DeleteView):
    model = Book
    
    success_url = reverse_lazy('book_list')