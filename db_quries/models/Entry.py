from datetime import date
from django.db import models
from django.db.models import CASCADE

from Blog import Blog
from Author import Author


class Entry(models.Model):

    blog = models.ForeignKey(Blog, on_delete=CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateTimeField()
    mod_date = models.DateTimeField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)