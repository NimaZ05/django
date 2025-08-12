from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=250)
    meesage = models.TextField()
    creted_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
