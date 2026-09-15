class Song:
    # Class Attributes to track global insights across all instances
    count = 0
    genres = []         # List to store unique genres
    artists = []        # List to store unique artists
    genre_count = {}    # Dictionary to keep track of song counts per genre
    artists_count = {}  # Dictionary to keep track of song counts per artist

    def __init__(self, name, artist, genre):
        # Instance Attributes
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Trigger class methods automatically upon a new song being created
        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artists_count(self.artist)

    @classmethod
    def add_song_to_count(cls):
        """Increments the value of count by one."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Adds any new genres to a class attribute genres. Ensures no duplicates."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Adds any new artists to a class attribute artists. Ensures no duplicates."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Updates class attribute genre_count dictionary tracking."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        """Updates class attribute artists_count dictionary tracking."""
        if artist in cls.artists_count:
            cls.artists_count[artist] += 1
        else:
            cls.artists_count[artist] = 1