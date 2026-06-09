class Song:
    # Class Attributes - Shared across all Song instances
    count = 0  # Total number of Song objects created
    genres = []  # List of unique genres from all songs
    artists = []  # List of unique artists from all songs
    genre_count = {}  # Dictionary: genre -> number of songs in that genre
    artist_count = {}  # Dictionary: artist -> number of songs by that artist

    def __init__(self, name, artist, genre):
        """
        Initialize a new Song object.
        
        Args:
            name (str): The song title
            artist (str): The artist name
            genre (str): The music genre
        """
        # Instance Attributes
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Trigger class methods to update global tracking
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """
        Increments the total count of Song objects by 1.
        Called automatically when a new song is created.
        """
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """
        Adds a new genre to the genres list if it doesn't already exist.
        Ensures unique genres only - no duplicates.
        
        Args:
            genre (str): Genre to add
        """
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """
        Adds a new artist to the artists list if they don't already exist.
        Ensures unique artists only - no duplicates.
        
        Args:
            artist (str): Artist name to add
        """
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """
        Updates the genre_count dictionary.
        Increments genre count by 1 if genre exists,
        otherwise adds the genre key and sets it to 1.
        
        Args:
            genre (str): Genre to increment count for
        """
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """
        Updates the artist_count dictionary.
        Increments artist count by 1 if artist exists,
        otherwise adds the artist key and sets it to 1.
        
        Args:
            artist (str): Artist to increment count for
        """
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

    @classmethod
    def get_song_count(cls):
        """
        Returns the total number of Song objects created.
        
        Returns:
            int: Total song count
        """
        return cls.count

    @classmethod
    def get_all_genres(cls):
        """
        Returns all unique genres from existing songs.
        
        Returns:
            list: List of unique genres
        """
        return cls.genres

    @classmethod
    def get_all_artists(cls):
        """
        Returns all unique artists from existing songs.
        
        Returns:
            list: List of unique artists
        """
        return cls.artists

    @classmethod
    def get_genre_count(cls):
        """
        Returns dictionary of genre counts.
        
        Returns:
            dict: Genre -> count mapping
        """
        return cls.genre_count

    @classmethod
    def get_artist_count(cls):
        """
        Returns dictionary of artist counts.
        
        Returns:
            dict: Artist -> count mapping
        """
        return cls.artist_count

    @classmethod
    def reset_all(cls):
        """
        Resets all class attributes (useful for testing).
        """
        cls.count = 0
        cls.genres = []
        cls.artists = []
        cls.genre_count = {}
        cls.artist_count = {}
