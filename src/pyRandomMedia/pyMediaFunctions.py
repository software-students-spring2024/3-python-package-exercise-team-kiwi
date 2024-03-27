import random
import feedparser
import pandas as pd
from src.pyRandomMedia.songs_file import songs
from src.pyRandomMedia.movies_file import movies

def get_song(genre, artist=None, song_name=None, release_date=None):
    if type(genre) != str or (artist is not None and type(artist) != str) or (song_name is not None and type(song_name) != str) or (release_date is not None and type(release_date) != str):
        raise TypeError("Please input strings only (including the release date!!)")
    possible_songs = {}
    for song in songs.keys():
        if genre in songs[song]["genre"]:
            if artist == None or artist in songs[song]["artist"]:
                if song_name == None or song_name in song:
                    if release_date == None or songs[song]["release_date"][:4] == release_date:
                        possible_songs[song] = songs[song]
    if possible_songs:
        return random.choice(list(possible_songs.items()))
    else:
        return "No songs found in our list"

def get_movie():
    randNum = random.randint(0,len(movies)-1)
    count = 0
    for i in movies:
        if count == randNum:
            movie_Name = i
            movie_Director = movies.get(i).get("director")
            movie_Star1 = movies.get(i).get("star_1")
            movie_Star2 = movies.get(i).get("star_2")
            movie_Star3 = movies.get(i).get("star_3")
            movie_Release_Year = movies.get(i).get("release_year")
            movie_Genre = movies.get(i).get("genre")
            randMovie = {
                'movieName':movie_Name,
                'movieDirector': movie_Director,
                'movieStar1':movie_Star1,
                'movieStar2':movie_Star2,
                'movieStar3':movie_Star3,
                'movieGenre': movie_Genre,
                'movieReleaseYear': movie_Release_Year
            }
            return randMovie
        count+=1



""" 
inputObj is the object which holds function options;

Sample input:
{
"inTitle": "Dam", #String in title of article
"num": 15, #Max number of articles to return. 
}
"""

def get_news(inputObj = {}):

    # Fetch the RSS feed
    feed = feedparser.parse('https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en');

    # Initialize an empty list to store parsed items
    parsed_items = []

    #keep count of items for num; 
    count = 0; 

    # Iterate over each item in the feed and parse relevant data
    for item in feed.entries:

        parsed_item = {
            'title': item.title,
            'link': item.link,
            'pubDate': item.published,
            'source': {
                'url': item.source.url,
                'name': item.source.title
            }
        }

        if("inTitle" in inputObj.keys()):
        
            if(inputObj["inTitle"] in parsed_item["title"]):
                parsed_items.append(parsed_item)
                count+=1
        else:
            parsed_items.append(parsed_item)
            count+=1

        if("num" in inputObj.keys() and count == inputObj["num"]):
            return parsed_items
        

    # Convert the parsed items list to JSON format
    return parsed_items


def get_random_TV_show():
    data = pd.read_csv('src/pyRandomMedia/netflix_titles.csv')
    data = data[(data['type'] == 'TV Show') & (data['director'].notnull()) & (data['cast'].notnull()) & (data['release_year'].notnull())]
    data = data.reset_index(drop=True)

    rand = random.randint(0, len(data) - 1)
    dic = data.iloc[rand][['title', 'director', 'cast', 'release_year']].to_dict()
    return dic
