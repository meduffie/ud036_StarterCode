import media
import fresh_tomatoes

#Each of these objects is a movie, the params being the details of the movie
#This data is used by fresh_tomatoes.py to build the website
perks_of_being_a_wallflower = media.Movie("Perks of Being a Wallflower",
                            "Socially awkward teen Charlie (Logan Lerman) is a wallflower, \
                            always watching life from the sidelines, until two charismatic students become his mentors.",
                            "http://t0.gstatic.com/images?q=tbn:ANd9GcSOWoRAyGn9rdRunV_Z2zFiQxI78NDrTkyLKwe8_ImeUkxp7cGl",
                            "https://www.youtube.com/watch?v=n5rh7O4IDc0")

v_for_vendetta = media.Movie("V for Vendetta", "In a future British tyranny, a shadowy freedom \
                            fighter, known only by the alias of \"V\", plots to overthrow it with \
                            the help of a young woman.", "http://www.gstatic.com/tv/thumb/movieposters/159693/p159693_p_v8_av.jpg",
                             "https://www.youtube.com/watch?v=k_13fFIrhPk")

nineteen_eighty_four = media.Movie("1984", "A man loses his identity while living under a repressive regime.",
                   "https://upload.wikimedia.org/wikipedia/en/c/c4/Nineteen_Eighty_Four.jpg",
                   "https://www.youtube.com/watch?v=Z4rBDUJTnNU")

#This list is made so that we can pass the objects to the open_movies_page
#function within fresh_tomatoes.py
movie_list = [perks_of_being_a_wallflower, v_for_vendetta, nineteen_eighty_four]

fresh_tomatoes.open_movies_page(movie_list)
