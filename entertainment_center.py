import fresh_tomatoes
import movie

# instantiation of movies by giving arguments 
movie1 = movie.Movie(
        'Avengers: Infinity War',
        'Movie about superheroes and one giant purple villain',
        'https://news.marvel.com/wp-content/uploads/2017/07/studios_post_master-960x540.jpg',      # noqa
        'https://www.youtube.com/watch?v=6ZfuNTqbHE8'
        )
movie2 = movie.Movie(
        'The New Mutants',
        'Movie about teenage X-men',
        'http://t2.gstatic.com/images?q=tbn:ANd9GcR3OXGa2wVRnoOiqcnpcpNuQJ7ue5C38JlqOkqnnTZvWa2UVVRk',      # noqa                    
        'https://www.youtube.com/watch?v=bu9e410C__I'
        )
movie3 = movie.Movie(
        'Ant Man and the Wasp',
        'Movie about guy that turns into an ant',
        'http://t2.gstatic.com/images?q=tbn:ANd9GcRxIQHv1T0L649pKR64-WOZpiWGKw5R7W7hkxK2Crl3EiQwZEja',   # noqa
        'https://www.youtube.com/watch?v=XyZERzqh090'
        )
# put all movie objects created into a list
movies = [movie1, movie2, movie3]

# open_movies_page takes in a list of movie objects
fresh_tomatoes.open_movies_page(movies) 
print(movie.Movie.__doc__)
