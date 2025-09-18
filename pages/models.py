from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=250, blank=True, null=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"

class Newsletter(models.Model):
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)

        
    def __str__(self):
        return self.email