from django.shortcuts import render
import requests

from .models import PopularMovie

from .secrets import movie_apikey, popular_apikey


def index(request):
    movies = []
    ids = []

    popular_url = 'https://api.themoviedb.org/3/movie/popular?api_key={}&language=en-US&page=1'.format(popular_apikey)
    r = requests.get(popular_url).json()
    print("# Getting movie list...")

    for movie in r['results'][:6]:

        ids.append(movie['id'])

        if PopularMovie.objects.filter(movie_id=movie['id']).exists():
            print("# Movie already in database...")
            pass
        else:
            popular_movie = {
                'title': movie['title'],
                'popularity': movie['popularity'],
                'id': movie['id'],
                'imdb_id': requests.get('https://api.themoviedb.org/3/movie/{}/external_ids?api_key={}'.format(movie['id'], popular_apikey)).json()['imdb_id'],
                'poster': None
            }

            popular_movie.update({'poster': requests.get('http://www.omdbapi.com/?apikey={}&i={}'.format(movie_apikey, popular_movie['imdb_id'])).json()['Poster']})

            result = PopularMovie(movie_id=popular_movie['id'], imdb_id=popular_movie['imdb_id'], title=popular_movie['title'], popularity=popular_movie['popularity'], poster=popular_movie['poster'])
            result.save()
            print("# Movie not in database; added...")

    for id in ids:
        results = PopularMovie.objects.filter(movie_id=id)
        for result in results:
            movie = {
                'title': result.title,
                'id': result.movie_id,
                'imdb_id': result.imdb_id,
                'poster': result.poster
            }
            movies.append(movie)

    context = {'results' : movies}
    return render(request, 'movies/index.html', context)