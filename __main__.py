from src.pyRandomMedia.pyMediaFunctions import get_song
from src.pyRandomMedia.pyMediaFunctions import get_news
from src.pyRandomMedia.pyMediaFunctions import get_random_TV_show
from src.pyRandomMedia.pyMediaFunctions import get_movie

fav_song = get_song("Pop", artist="One")

if type(fav_song) != str:
      print(fav_song)
else:
      print("I don't have a favorite song.")


inTitleString = "a"
curr = get_news({ "inTitle": inTitleString, "num": 5 })
print(curr)

tv_show = get_random_TV_show(['title', 'director', 'cast', 'release_year'])
print(tv_show)

movie = get_movie("action")
print(movie)