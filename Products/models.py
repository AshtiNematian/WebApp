from django.db import models


# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=250)
    picture = models.ImageField(upload_to='Images')
    description = models.TextField()
    published = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return self.title
