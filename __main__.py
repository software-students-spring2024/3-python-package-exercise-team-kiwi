from src.pyRandomMedia.pyMediaFunctions import get_song
from src.pyRandomMedia.pyMediaFunctions import get_news
from src.pyRandomMedia.pyMediaFunctions import get_random_TV_show

fav_song = get_song("Pop")

if type(fav_song) != str:
      print(f'My favorite song is {fav_song[0]} by {fav_song[1]["artist"]}. ' 
            f'Its genre is {fav_song[1]["genre"]} and it was released on {fav_song[1]["release_date"]}')
else:
      print("I don't have a favorite song.")


inTitleString = "a"
curr = get_news({ "inTitle": inTitleString, "num": 5 })
print(curr);

tv_show = get_random_TV_show()
print(tv_show)
