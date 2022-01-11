from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class Book(models.Model):
    name = models.CharField( max_length=50)
    price = models.DecimalField( max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to="image")
    created = models.DateTimeField(auto_now=False, auto_now_add=False)
    favorite = models.ManyToManyField(User, related_name='favorite' , blank=True)
   
    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")

    ordering = ('name',)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(_("name"), max_length=50)
    image = models.ImageField(_("image"), upload_to='clients', blank=True , null=True)
    description = models.TextField(_("description"))


    

    class Meta:
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")

    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(_("title"), max_length=50)
    description = models.TextField(_("description"))
    image = models.ImageField(_("image"), upload_to='posts', blank=True , null=True)

    

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title
