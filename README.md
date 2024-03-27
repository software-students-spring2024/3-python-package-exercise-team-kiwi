# PyMedia

![Python build & run test](https://github.com/software-students-spring2024/3-python-package-exercise-team-kiwi/actions/workflows/build.yaml/badge.svg)

## Concept
We wanted to create a package that allows users to generate different kinds of media. We figured this kind of package could potentially be used to easily populate datasets or to generate lists of certain types of media that are popular right now (assuming we keep our datasets updated). The package comes with four functions that allow users to return different songs, movies, TV shows, and current events. 

## Installation
Sang

## Usage
Once installed and imported, you can call each function to generate a certain kind of media.

### get_song()
You can call the get_song() function to generate a song in a specific genre, with optional specifications for the artist/band names, song title, and release date. All inputs must be strings. 

![get_song() example](./images/song_example.png)

The variable fav_song will now contain a tuple holding a song in the Pop genre by an artist/band with the word "One" in it. An example tuple would look like this: 
![song output](./images/song_output.png)

Additionally, if no song meeting the arguments' criteria is found, get_song() will return a string. 

### get_news()

You can call the get_news() function to generate a list of current events. The function takes a dictionary as an argument that optionally allows the user to only return a certain number of events as well as news title with a certain string in them. 

![get_news() example](./images/news_example.png)

The variable curr will now contain a list of 5 current news stories whose titles have the string "a" in them. Each news story is represented as a dictionary:

![news story output](./images/news_output.png)

### get_movie()

You can call the get_movie() function to generate a movie in a specific genre. 

![get_movie() example](./images/movie_example.png)

The variable movie will now contain a dictionary holding a movie in the action genre. An example of dictionary would look like this:

![movie output](./images/movie_output.png)

### get_random_TV_show()

Sang- just copy the format above for your function

## Function Documentation
Sang
Include link to example program here too

## How to contribute
Stan

## Team members

Stanley Moukhametzianov (SM9231) [Github Profile](https://github.com/Stanley-Moukhametzianov)
<br>
Benson Li (BL2995) [Github Profile](https://github.com/bensonnli)
<br>
Nicholas Meng (ndm9914) [Github Profile](https://github.com/Nmeng01)
<br>
Sangeyl Lee (SL6733) [Github Profile](https://github.com/S2ang) 

Here's the link to our package on PyPI: