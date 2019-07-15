# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Import Generic View for listing (r operation)
from django.views.generic import ListView, DetailView

# Import Generic View for creating, updating and deleting (cud operations)
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Resolving URLs
from django.urls import reverse_lazy

# Import Book Model
from book.models import Book

# Import Book Form
from book.forms import BookForm

# List View
class BookList(ListView):
    model = Book

# Detail View
class BookView(DetailView):
    model = Book

# Create View
class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    # Setting returning URL
    success_url = reverse_lazy('book_list')

# Update View
class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    # Setting returning URL
    success_url = reverse_lazy('book_list')

# Delete View
class BookDelete(DeleteView):
    model = Book
    # Setting returning URL
    success_url = reverse_lazy('book_list')