import random
from src.pyRandomMedia.songs_file import songs

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

