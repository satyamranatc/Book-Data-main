from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200)
    cover_image = models.ImageField(upload_to='covers/')
    pdf = models.FileField(upload_to='pdfs/')
    
    def __str__(self):
        return self.name
