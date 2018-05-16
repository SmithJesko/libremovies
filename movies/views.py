from django.shortcuts import render
import requests

from .models import SearchResult


def index(request):
    movies = []

    url = 'http://www.omdbapi.com/?apikey={}&s=${}&plot=full'.format('d30f5732', 'home+alone')
    r = requests.get(url).json()
    # print(r)

    for movie in r['Search']:
        movie_info = {
            'title': movie['Title'],
            'year': movie['Year'],
            'imdb_id': movie['imdbID'],
            'poster': movie['Poster'],
            # 'genre': movie['Genre'],
            # 'released': movie['Released'],
            # 'rated': movie['Rated'],
            # 'imdb_rating': movie['imdbRating'],
            # 'director': movie['Director'],
            # 'writer': movie['Writer'],
            # 'actors': movie['Actors'],
            # 'plot': movie['Plot'],
        }
        movies.append(movie_info)  

        if SearchResult.objects.filter(imdb_id=movie_info['imdb_id']).exists():
            pass
        else:
            result = SearchResult(imdb_id=movie_info['imdb_id'], title=movie_info['title'], year=movie_info['year'], poster=movie_info['poster'])
            result.save()

    context = {'results' : movies}
    return render(request, 'movies/index.html', context)