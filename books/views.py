from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
import datetime
from books.models import Book, Chapter, Section
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.shortcuts import get_object_or_404
# Create your views here.

class BookDetailView(DetailView):
    model = Book
    template_name = 'preview.html'
    context_object_name = 'book'

class ChapterEntry(CreateView):
    model = Chapter
    fields = ['title']
    template_name = 'create-chapter.html'

    def form_valid(self, form):
        form.instance.book = Book.objects.get(id = self.kwargs['book_id'] )
        return super().form_valid(form)

    
    def  get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = Book.objects.get(id = self.kwargs['book_id'] )
        context["book"] = book
        return context

    def get_success_url(self, **kwargs):
        return reverse("book-detail", kwargs={'pk': self.object.book.pk})

class SectionEntry(CreateView):
    model = Section
    fields = [ 'title', 'image', 'text_content']
    template_name = 'create-section.html'

    def form_valid(self, form):
        form.instance.chapter = Chapter.objects.get(id = self.kwargs['chapter_id'] )
        return super().form_valid(form)
    
    def  get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        chapter = Chapter.objects.get(id = self.kwargs['chapter_id'] )
        context["chapter"] = chapter
        context["book"] = chapter.book
        return context

    def get_success_url(self, **kwargs):
        return reverse("book-detail", kwargs={'pk': self.object.chapter.book.pk})
    

























def create_new_book(request):
    #code for creating a new book
    pass

def book_list(request):
    #code to show all books
    pass

def book_details(request):
    #code to show the details of a single book
    pass

def book_update(request):
    #code to update data of a book
    pass