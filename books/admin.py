from django.contrib import admin
from books.models import Book, Chapter, Section
# Register your models here.
admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Section)