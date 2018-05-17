from django.db import models


class PopularMovie(models.Model):
    movie_id = models.CharField(max_length=20)
    imdb_id = models.CharField(max_length=20)
    title = models.CharField(max_length=150)
    year = models.CharField(max_length=10)
    poster = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'PopularMovie'
        verbose_name_plural = 'PopularMovies'

class Movie(models.Model):
    pass