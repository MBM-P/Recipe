from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    ingredients = models.TextField()
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.title
