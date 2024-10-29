from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic import ListView
# Create your views here.

class BookListView(ListView):
    model = Book

book_detail = BookDetail.as_view()