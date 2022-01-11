from django.shortcuts import get_list_or_404, render

# Create your views here.
from .models import Book , Client , Post

def index(request):
    books = Book.objects.all()
    clients = Client.objects.all()
    posts = Post.objects.all()

    context = {
        'books': books,
        'clients': clients,
        'posts': posts,
  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    }
    return render(request , 'index.html' , context)