from django.db import models


class SearchResult(models.Model):
    imdb_id = models.CharField(max_length=20)
    title = models.CharField(max_length=150)
    year = models.CharField(max_length=10)
    poster = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'SearchResult'
        verbose_name_plural = 'SearchResults'

class Movie(models.Model):
    pass