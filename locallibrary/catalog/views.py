from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre

def index(request):
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    txt_search = '할랄'
    num_books_genre = Book.objects.filter(title__contains=txt_search).count()

    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()

    # Number of visits to this view, as counted in the session variable.
    # request.session.get("session name", "setting the value to 0 if it has not previously been set")
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'txt_search' : txt_search,
        'num_books_genre': num_books_genre,
        'num_visits' : num_visits
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

# Django-Best-Practice
from django.views import generic

class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author