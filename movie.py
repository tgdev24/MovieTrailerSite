import webbrowser


class Movie():    
    """ Class that sets the title, storyline, poster image, and trailer url
        to movie objects """
    def __init__(self, movie_title, storyline, poster_image_url, trailer_url):
        """ Constructor for the Movie class """
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_url
        
    def show_trailer(self):
        """ Opens up the trailer at the designated url """
        webbrowser.open(self.trailer_url)