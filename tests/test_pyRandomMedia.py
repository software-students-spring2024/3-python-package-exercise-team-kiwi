import pytest
from src.pyRandomMedia.pyMediaFunctions import get_song

class Tests:
    def test_sanity_check(self):
        expected = True  # the value we expect to be present
        actual = True  # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"
    
    def test_song_inputs(self):
        actual = get_song("Pop")[1]["genre"]
        assert "Pop" in actual, f"Expected the genre to contain the word Pop, but {actual} does not contain Pop."
        actual = get_song("Hip Hop", artist="Eminem")
        assert "Hip Hop" in actual[1]["genre"] and "Eminem" in actual[1]["artist"], f"Expected the genre string to contain Hip Hop and the artist string to contain Eminem, but {actual} does not fulfill these conditions."
        actual = get_song("Pop", song_name="Stressed")
        assert "Stressed" in actual[0] and "Pop" in actual[1]["genre"], f"Expected the name of the song to contain Stressed and the genre to contain Pop, but {actual} does not fulfill these conditions"

    def test_type_error(self):
        with pytest.raises(TypeError):
            get_song("Pop", release_date=2011)
    
    def test_song_not_found(self):
        actual = get_song("Grime")
        assert actual == "No songs found in our list", f"Expected to not find a song because there are no Grime songs in songs_file, but {actual} was found."
    
