from django.db import models
from taggit.managers import TaggableManager
from Accounts.models import User


class Post(models.Model):
    CATEGORIES = [('frontend', 'FrontEnd'),
                  ('backend', 'BackEnd'),
                  ('digital marketing', 'Digital Marketing'),
                  ('technological reports', 'Technological Reports'),
                  ('entertainment', 'Entertainment')]
    title = models.CharField(max_length=250)
    description = models.TextField()
    category = models.CharField(choices=CATEGORIES, max_length=50, default='unknown')
    published = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=100)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    tags = TaggableManager()

    def get_tags(self):
        """ names() is a django-taggit method, returning a ValuesListQuerySet
        (basically just an iterable) containing the name of each tag as a string
        """
        return self.tags.names()

    def __str__(self):
        return self.title
