class Movie():
    """ This class defines the Movie type, which stores information
        like titles, youtube trailers, etc about movies """
    
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """ This constructor takes the given params when objects of
            the movie type are created and sets them to the proper
            instance variables """
        
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
