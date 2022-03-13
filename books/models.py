from django.db import models
from django.urls import reverse
# Create your models here.

class Book(models.Model):
    title = models.CharField( max_length = 50)
    description = models.TextField(null = True)
    
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['title']
    

class Chapter(models.Model):
    book = models.ForeignKey(to = "books.Book", on_delete=models.PROTECT)
    title = models.CharField( max_length = 50)
    serial = models.PositiveIntegerField()
    

    
    def get_absolute_url(self):
        return reverse("chapter_detail", kwargs={"pk": self.pk})

    def save(self):
        if self.serial != None and Chapter.objects.filter(book = self.book, serial = self.serial).exists:
            raise ValueError('Serial Already Exists')
        last_chapter = Chapter.objects.filter(book = self.book).last()
        if last_chapter == None:
            self.serial =  1
        else: 
            self.serial = last_chapter.serial + 1
        return super().save()


    def __str__(self):
        return f'{self.book}:{self.title}'
    
    class Meta:
        ordering = ['serial']
      

class Section(models.Model):
    chapter = models.ForeignKey(to = "books.Chapter", on_delete=models.PROTECT)
    title = models.CharField( max_length = 50)
    text_content =  models.TextField( default= 'no text content')
    image = models.ImageField(null = True, blank = True )
    serial = models.PositiveIntegerField()
    
    def save(self):
        if self.serial != None and Section.objects.filter(chapter = self.chapter, serial = self.serial).exists:
            raise ValueError('Serial Already Exists')
        last_section = Section.objects.filter(chapter = self.chapter).last()
        if last_section == None:
            self.serial = 1
        else: 
            self.serial = last_section.serial + 1
        return super().save()
    def __str__(self):
        return f'{self.chapter}:{self.title}'
    
    class Meta:
        ordering = ['serial']