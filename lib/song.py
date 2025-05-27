class Song:
     # CLASS ATTRIBUTES
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # INSTANCE ATTRIBUTES
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class‐level tracking
        Song._add_song_to_count()
        Song._add_to_artists(artist)
        Song._add_to_genres(genre)
        Song._add_to_artist_count(artist)
        Song._add_to_genre_count(genre)

    # —— CLASS METHODS FOR TRACKING —— #

    @classmethod
    def _add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def _add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def _add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def _add_to_artist_count(cls, artist):
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1

    @classmethod
    def _add_to_genre_count(cls, genre):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1
