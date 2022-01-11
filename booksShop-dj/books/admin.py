from django.contrib import admin

# Register your models here.
from .models import Book , Client , Post

admin.site.register(Book)
admin.site.register(Client)
admin.site.register(Post)