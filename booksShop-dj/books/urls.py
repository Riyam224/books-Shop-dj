from django.urls import path
from . import views 



urlpatterns = [
    path('' , views.index , name='index'),
    # path('book_favorite_list/' , views.book_favorite_list , name='book_favorite_list')
]
