from pyrandommedia import get_news
from pyrandommedia import get_random_TV_show
from pyrandommedia import get_song
from pyrandommedia import get_movie
print(get_news({"num":2}));
print(get_song("Pop"));

tv_show = get_random_TV_show(['title', 'director', 'cast'])
print(tv_show)

movie = get_movie("action")
print(movie)

movie2 = get_movie("animation")
print(movie2)

movie2 = get_movie("crime")
print(movie2)