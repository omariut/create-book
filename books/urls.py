
from django.contrib import admin
from django.urls import path
from books import views
urlpatterns = [
    path('<int:pk>', views.BookDetailView.as_view() , name = 'book-detail'),
    path('create-section', views.SectionEntry.as_view() , name = 'create-section'),
    path('create-chapter', views.ChapterEntry.as_view() , name = 'create-chapter'),
    path('create-chapter/<int:book_id>/', views.ChapterEntry.as_view() , name = 'create-chapter-of-book'),
    path('create-section/<int:chapter_id>/', views.SectionEntry.as_view() , name = 'create-section-of-chapter'),

]






    
    # #CRUD (Create, Read, Update, Delete)
    # path('new', name = 'new_book'),
    # path('list', name = 'book_list'),
    # path('/<int:pk>', name ='book_details'),
    # path('/<int:pk>', name = 'book_update'),
    # path('/<int:pk>', name = 'book_delete'),