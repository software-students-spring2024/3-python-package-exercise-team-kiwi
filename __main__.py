from src.pyRandomMedia.pyMediaFunctions import get_song
from src.pyRandomMedia.pyMediaFunctions import get_news
from src.pyRandomMedia.pyMediaFunctions import get_random_TV_show
from src.pyRandomMedia.pyMediaFunctions import get_movie

fav_song = get_song("Pop")

if type(fav_song) != str:
      print(f'My favorite song is {fav_song[0]} by {fav_song[1]["artist"]}. ' 
            f'Its genre is {fav_song[1]["genre"]} and it was released on {fav_song[1]["release_date"]}')
else:
      print("I don't have a favorite song.")


inTitleString = "a"
curr = get_news({ "inTitle": inTitleString, "num": 5 })
print(curr)

tv_show = get_random_TV_show(['title', 'director', 'cast', 'release_year'])
print(tv_show)

movie = get_movie()
print(f'Your movie is {movie.get("movieName")}, directed by {movie.get("movieDirector")}, starring {movie.get("movieStar1")}, {movie.get("movieStar2")}, and {movie.get("movieStar3")}. This {movie.get("movieGenre")} movie was released in {movie.get("movieReleaseYear")}.')
print(movie)